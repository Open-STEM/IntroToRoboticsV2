import os
import json
import copy
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import google.generativeai
from dotenv import load_dotenv
from prompt_manager import PromptManager

@dataclass
class FeedbackSummary:
    """Summarized feedback from grader and link checker"""
    grader_grade: str
    grader_issues: List[str]
    link_issues: List[str]
    overall_score: float
    conversation_turn: int

@dataclass
class PromptModification:
    """A specific modification to make to the prompt"""
    section: str
    current_text: str
    suggested_text: str
    reason: str
    confidence: float

class PromptEditor:
    """Agent that automatically improves tutor prompts based on feedback"""
    
    def __init__(self, prompt_file: str = "tutor_prompt.txt"):
        self.prompt_manager = PromptManager()
        self.prompt_file = prompt_file
        self.current_prompt = self._load_current_prompt()
        self.performance_history = []
        
        # Setup Gemini for prompt analysis and editing
        load_dotenv()
        api_key = os.getenv('GOOGLE_AI_API_KEY')
        if api_key:
            google.generativeai.configure(api_key=api_key)
            self.model = google.generativeai.GenerativeModel(model_name="gemini-2.5-pro")
        else:
            self.model = None
            print("Warning: No API key found, prompt editing will be limited")
        
        # Define prompt sections for targeted editing
        self.prompt_sections = self._identify_prompt_sections()
    
    def _load_current_prompt(self) -> str:
        """Load current prompt from file"""
        try:
            return self.prompt_manager.load_prompt(self.prompt_file)
        except FileNotFoundError:
            print(f"Warning: Prompt file '{self.prompt_file}' not found.")
            return ""
    
    def _identify_prompt_sections(self) -> Dict[str, str]:
        """Identify and extract key sections from the prompt for targeted editing"""
        sections = {}
        
        # Split prompt into major sections based on headers
        current_section = "HEADER"
        current_content = []
        
        for line in self.current_prompt.split('\n'):
            if line.strip().startswith('**') and line.strip().endswith(':**'):
                # Save previous section
                if current_content:
                    sections[current_section] = '\n'.join(current_content)
                
                # Start new section
                current_section = line.strip('*: ')
                current_content = [line]
            else:
                current_content.append(line)
        
        # Save final section
        if current_content:
            sections[current_section] = '\n'.join(current_content)
        
        return sections
    
    def analyze_feedback(self, feedback_summary: FeedbackSummary) -> List[str]:
        """Analyze feedback to identify specific areas for prompt improvement"""
        if not self.model:
            return ["No analysis model available"]
        
        analysis_prompt = f"""You are an expert prompt engineer analyzing feedback about an AI tutor's performance. Based on the feedback below, identify specific areas where the tutor's system prompt should be improved.

GRADER FEEDBACK:
Grade: {feedback_summary.grader_grade}
Issues Identified: {'; '.join(feedback_summary.grader_issues) if feedback_summary.grader_issues else 'None specified'}

LINK CHECKER FEEDBACK:
Link Issues: {'; '.join(feedback_summary.link_issues) if feedback_summary.link_issues else 'None'}
Overall Link Score: {feedback_summary.overall_score}

CURRENT PROMPT SECTIONS AVAILABLE FOR EDITING:
{', '.join(self.prompt_sections.keys())}

Instructions:
1. Identify which prompt sections might need improvement based on the feedback
2. Suggest specific problems that could be addressed
3. Focus on actionable improvements, not general praise

Respond with a bulleted list of specific improvement areas:
- Section: [SECTION_NAME] - Problem: [SPECIFIC_ISSUE] - Impact: [HIGH/MEDIUM/LOW]

Analysis:"""

        try:
            response = self.model.generate_content(analysis_prompt)
            improvement_areas = []
            
            for line in response.text.split('\n'):
                if line.strip().startswith('-') and 'Section:' in line:
                    improvement_areas.append(line.strip('- '))
            
            return improvement_areas if improvement_areas else ["No specific improvements identified"]
        
        except Exception as e:
            return [f"Error analyzing feedback: {str(e)}"]
    
    def generate_prompt_modifications(self, improvement_areas: List[str]) -> List[PromptModification]:
        """Generate specific modifications to the prompt based on improvement areas"""
        modifications = []
        
        if not self.model:
            return modifications
        
        for area in improvement_areas:
            try:
                # Extract section name from improvement area
                section_name = area.split('Section:')[1].split('-')[0].strip() if 'Section:' in area else "GENERAL"
                
                if section_name not in self.prompt_sections and section_name != "GENERAL":
                    continue
                
                current_section_text = self.prompt_sections.get(section_name, "")
                
                modification_prompt = f"""You are an expert prompt engineer. Improve this specific section of an AI tutor prompt based on the identified issue.

IMPROVEMENT AREA: {area}

CURRENT SECTION TEXT:
{current_section_text}

Instructions:
1. Propose a specific, actionable modification to address the identified issue
2. Keep the overall structure and style consistent
3. Make targeted improvements, not wholesale rewrites
4. Maintain the educational focus

Respond in this exact format:
CONFIDENCE: [0.0-1.0]
REASON: [Brief explanation of why this change helps]
MODIFIED_TEXT:
[Your improved version of the section]"""

                response = self.model.generate_content(modification_prompt)
                result_text = response.text.strip()
                
                # Parse response
                if "CONFIDENCE:" in result_text and "MODIFIED_TEXT:" in result_text:
                    confidence_line = result_text.split("CONFIDENCE:")[1].split("\n")[0].strip()
                    confidence = float(confidence_line) if confidence_line.replace(".", "").isdigit() else 0.5
                    
                    reason = result_text.split("REASON:")[1].split("MODIFIED_TEXT:")[0].strip()
                    modified_text = result_text.split("MODIFIED_TEXT:")[1].strip()
                    
                    modifications.append(PromptModification(
                        section=section_name,
                        current_text=current_section_text,
                        suggested_text=modified_text,
                        reason=reason,
                        confidence=confidence
                    ))
            
            except Exception as e:
                print(f"Error generating modification for {area}: {e}")
                continue
        
        return modifications
    
    def apply_modifications(self, modifications: List[PromptModification], min_confidence: float = 0.7) -> bool:
        """Apply modifications to the prompt if they meet confidence threshold"""
        applied_any = False
        new_prompt = self.current_prompt
        
        # Sort by confidence, apply highest confidence changes first
        sorted_mods = sorted(modifications, key=lambda x: x.confidence, reverse=True)
        
        for mod in sorted_mods:
            if mod.confidence >= min_confidence:
                if mod.section in self.prompt_sections:
                    # Replace the section in the full prompt
                    old_section = self.prompt_sections[mod.section]
                    new_prompt = new_prompt.replace(old_section, mod.suggested_text)
                    print(f"Applied modification to {mod.section} (confidence: {mod.confidence:.2f})")
                    applied_any = True
                else:
                    print(f"Skipped modification to unknown section: {mod.section}")
            else:
                print(f"Skipped low-confidence modification to {mod.section} (confidence: {mod.confidence:.2f})")
        
        if applied_any:
            # Update current prompt and save to file
            self.current_prompt = new_prompt
            self.prompt_sections = self._identify_prompt_sections()  # Re-identify sections
            
            # Save the updated prompt to file
            success = self.prompt_manager.save_prompt(self.prompt_file, new_prompt)
            if success:
                print(f"Updated prompt saved to {self.prompt_file}")
            else:
                print(f"Failed to save updated prompt to {self.prompt_file}")
        
        return applied_any
    
    def process_feedback_and_improve(self, feedback_summary: FeedbackSummary, min_confidence: float = 0.7) -> Dict[str, any]:
        """Main method: analyze feedback and improve prompt"""
        
        # Store performance data
        self.performance_history.append({
            "turn": feedback_summary.conversation_turn,
            "grade": feedback_summary.grader_grade,
            "link_score": feedback_summary.overall_score,
            "timestamp": datetime.now()
        })
        
        # Analyze feedback for improvement opportunities
        improvement_areas = self.analyze_feedback(feedback_summary)
        
        # Generate specific modifications
        modifications = self.generate_prompt_modifications(improvement_areas)
        
        # Apply high-confidence modifications
        applied = self.apply_modifications(modifications, min_confidence)
        
        return {
            "improvement_areas": improvement_areas,
            "proposed_modifications": len(modifications),
            "applied_modifications": len([m for m in modifications if m.confidence >= min_confidence]),
            "prompt_updated": applied,
            "modifications_details": [
                {
                    "section": m.section,
                    "confidence": m.confidence,
                    "reason": m.reason,
                    "applied": m.confidence >= min_confidence
                }
                for m in modifications
            ]
        }
    
    def get_current_prompt(self) -> str:
        """Get the current version of the prompt"""
        return self.current_prompt
    
    def reload_from_file(self) -> bool:
        """Reload prompt from file (useful if externally modified)"""
        try:
            self.current_prompt = self._load_current_prompt()
            self.prompt_sections = self._identify_prompt_sections()
            print(f"Reloaded prompt from {self.prompt_file}")
            return True
        except Exception as e:
            print(f"Failed to reload prompt: {e}")
            return False
    
    def get_performance_summary(self) -> Dict[str, any]:
        """Get summary of performance trends"""
        if not self.performance_history:
            return {"message": "No performance data available"}
        
        recent_scores = [p["link_score"] for p in self.performance_history[-5:]]  # Last 5 conversations
        recent_grades = [p["grade"] for p in self.performance_history[-5:]]
        
        return {
            "total_conversations": len(self.performance_history),
            "recent_avg_link_score": sum(recent_scores) / len(recent_scores) if recent_scores else 0,
            "recent_grades": recent_grades,
            "performance_trend": "improving" if len(recent_scores) >= 2 and recent_scores[-1] > recent_scores[0] else "stable"
        }
