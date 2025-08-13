import re
import requests
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Tuple, Optional
import time
from dataclasses import dataclass
from bs4 import BeautifulSoup
import google.generativeai
from dotenv import load_dotenv
import os

@dataclass
class LinkCheckResult:
    """Result of checking a single link"""
    url: str
    status_code: Optional[int]
    is_accessible: bool
    content_snippet: str
    error_message: Optional[str]

@dataclass
class FactCheckResult:
    """Result of fact-checking content against a link"""
    claim: str
    source_url: str
    is_accurate: bool
    confidence_score: float  # 0-1
    explanation: str

class LinkChecker:
    """Agent that verifies links and fact-checks content against sources"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (XRP Course Link Checker Bot)'
        })
        
        # Setup Gemini for content analysis
        load_dotenv()
        api_key = os.getenv('GOOGLE_AI_API_KEY')
        if api_key:
            google.generativeai.configure(api_key=api_key)
            self.model = google.generativeai.GenerativeModel(model_name="gemini-2.5-flash")
        else:
            self.model = None
            print("Warning: No API key found, fact-checking will be limited")
    
    def extract_links_from_text(self, text: str) -> List[str]:
        """Extract all URLs from text using regex"""
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        
        # Also extract markdown-style links
        markdown_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        markdown_matches = re.findall(markdown_pattern, text)
        for _, url in markdown_matches:
            if url.startswith('http'):
                urls.append(url)
        
        return list(set(urls))  # Remove duplicates
    
    def check_link_accessibility(self, url: str, timeout: int = 10) -> LinkCheckResult:
        """Check if a link is accessible and extract content snippet"""
        try:
            response = self.session.get(url, timeout=timeout, allow_redirects=True)
            
            # Get content snippet
            content_snippet = ""
            if response.headers.get('content-type', '').startswith('text/html'):
                soup = BeautifulSoup(response.content, 'html.parser')
                # Remove script and style elements
                for script in soup(["script", "style"]):
                    script.decompose()
                content_snippet = soup.get_text()[:500]  # First 500 chars
            
            return LinkCheckResult(
                url=url,
                status_code=response.status_code,
                is_accessible=200 <= response.status_code < 400,
                content_snippet=content_snippet.strip(),
                error_message=None
            )
        
        except requests.exceptions.RequestException as e:
            return LinkCheckResult(
                url=url,
                status_code=None,
                is_accessible=False,
                content_snippet="",
                error_message=str(e)
            )
    
    def fact_check_claim_against_source(self, claim: str, source_url: str, source_content: str) -> FactCheckResult:
        """Use LLM to fact-check a claim against source content"""
        if not self.model:
            return FactCheckResult(
                claim=claim,
                source_url=source_url,
                is_accurate=True,  # Default to true if no model
                confidence_score=0.0,
                explanation="No fact-checking model available"
            )
        
        prompt = f"""You are a fact-checking assistant. Compare the following CLAIM against the SOURCE CONTENT and determine if the claim is accurate.

CLAIM: {claim}

SOURCE CONTENT: {source_content[:2000]}  # Limit content length

SOURCE URL: {source_url}

Instructions:
1. Determine if the claim is factually supported by the source content
2. Provide a confidence score from 0.0 (completely inaccurate) to 1.0 (completely accurate)
3. Give a brief explanation of your assessment

Respond in this exact format:
ACCURATE: [YES/NO]
CONFIDENCE: [0.0-1.0]
EXPLANATION: [Your brief explanation]"""

        try:
            response = self.model.generate_content(prompt)
            result_text = response.text.strip()
            
            # Parse response
            accurate = "YES" in result_text.split("ACCURATE:")[1].split("\n")[0].upper()
            confidence_line = result_text.split("CONFIDENCE:")[1].split("\n")[0].strip()
            confidence = float(confidence_line) if confidence_line.replace(".", "").isdigit() else 0.5
            explanation = result_text.split("EXPLANATION:")[1].strip() if "EXPLANATION:" in result_text else "No explanation provided"
            
            return FactCheckResult(
                claim=claim,
                source_url=source_url,
                is_accurate=accurate,
                confidence_score=confidence,
                explanation=explanation
            )
        
        except Exception as e:
            return FactCheckResult(
                claim=claim,
                source_url=source_url,
                is_accurate=True,  # Default to true on error
                confidence_score=0.0,
                explanation=f"Error during fact-checking: {str(e)}"
            )
    
    def check_tutor_response(self, tutor_response: str) -> Dict[str, any]:
        """Main method to check a tutor response for link accuracy and fact-checking"""
        results = {
            "link_checks": [],
            "fact_checks": [],
            "overall_score": 1.0,
            "issues_found": []
        }
        
        # Extract and check all links
        urls = self.extract_links_from_text(tutor_response)
        
        for url in urls:
            time.sleep(0.5)  # Rate limiting
            link_result = self.check_link_accessibility(url)
            results["link_checks"].append(link_result)
            
            if not link_result.is_accessible:
                results["issues_found"].append(f"Broken link: {url}")
                results["overall_score"] *= 0.8  # Penalize broken links
            
            # If link is accessible and has content, fact-check any claims about it
            if link_result.is_accessible and link_result.content_snippet:
                # Extract sentences that mention this URL or its domain
                domain = urlparse(url).netloc
                sentences = tutor_response.split('.')
                relevant_claims = [s.strip() for s in sentences if domain in s or url in s]
                
                for claim in relevant_claims:
                    if len(claim) > 10:  # Skip very short claims
                        fact_result = self.fact_check_claim_against_source(
                            claim, url, link_result.content_snippet
                        )
                        results["fact_checks"].append(fact_result)
                        
                        if not fact_result.is_accurate:
                            results["issues_found"].append(
                                f"Potentially inaccurate claim about {url}: {claim}"
                            )
                            results["overall_score"] *= (1 - (1 - fact_result.confidence_score) * 0.5)
        
        return results
    
    def generate_feedback_report(self, check_results: Dict[str, any]) -> str:
        """Generate a human-readable feedback report"""
        report = ["=== LINK CHECKER REPORT ===\n"]
        
        # Overall score
        score = check_results["overall_score"]
        report.append(f"Overall Link Accuracy Score: {score:.2f}/1.0\n")
        
        # Link accessibility results
        if check_results["link_checks"]:
            report.append("LINK ACCESSIBILITY:")
            for link_check in check_results["link_checks"]:
                status = "✓ ACCESSIBLE" if link_check.is_accessible else "✗ BROKEN"
                report.append(f"  {status}: {link_check.url}")
                if link_check.error_message:
                    report.append(f"    Error: {link_check.error_message}")
            report.append("")
        
        # Fact-checking results
        if check_results["fact_checks"]:
            report.append("FACT-CHECKING RESULTS:")
            for fact_check in check_results["fact_checks"]:
                accuracy = "✓ ACCURATE" if fact_check.is_accurate else "✗ QUESTIONABLE"
                report.append(f"  {accuracy} (conf: {fact_check.confidence_score:.2f}): {fact_check.claim[:100]}...")
                report.append(f"    Source: {fact_check.source_url}")
                report.append(f"    Explanation: {fact_check.explanation}")
            report.append("")
        
        # Issues summary
        if check_results["issues_found"]:
            report.append("ISSUES FOUND:")
            for issue in check_results["issues_found"]:
                report.append(f"  • {issue}")
        else:
            report.append("No major issues found with links or factual accuracy.")
        
        return "\n".join(report)



