"""XRP Tutoring Evaluation Bot - Evaluates and improves tutor performance"""

from google import genai
from google.genai import types
import pathlib, json, random, re, os
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GraderEvaluation(BaseModel):
    grade: str
    overall_feedback: str
    improvement_suggestions: list[str]
    strengths: list[str]
    prompt_adherence_score: int


class PromptEditSuggestion(BaseModel):
    updated_prompt: str
    changes_made: list[str]
    rationale: str


class XRPEvaluator:
    def __init__(self, api_key: str = None):
        if api_key is None:
            api_key = os.getenv('GOOGLE_AI_API_KEY')
            if not api_key:
                raise ValueError("GOOGLE_AI_API_KEY not found in environment variables! Please set it in your .env file or pass it directly.")
        self.client = genai.Client(api_key=api_key)
        self.feedback_history = self._load_json("feedback_history.json", [])
        self.questions = self._load_questions()
        
        curriculum = pathlib.Path("combined_documentation.md").read_text()
        prompts = {f.stem.split('_')[0]: pathlib.Path(f).read_text() 
                  for f in pathlib.Path('.').glob('prompts/*_prompt.txt')}
        
        self.configs = {role: types.GenerateContentConfig(
            system_instruction=f"{prompts[role]}\n\nDOCS:\n{curriculum}" if role in ['expert', 'tutor'] 
            else prompts[role],
            response_mime_type="application/json" if role in ['grader', 'editor'] else None,
            response_schema=GraderEvaluation if role == 'grader' else 
                          PromptEditSuggestion if role == 'editor' else None
        ) for role in ['expert', 'tutor', 'student', 'grader', 'editor']}
    
    def _load_json(self, file: str, default):
        try: return json.loads(pathlib.Path(file).read_text())
        except: return default
    
    def _save_json(self, file: str, data):
        pathlib.Path(file).write_text(json.dumps(data, indent=2))
    
    def _load_questions(self):
        try:
            content = pathlib.Path("faq.txt").read_text()
            return re.findall(r'^\d+\.\s*(.+)$', content, re.MULTILINE)
        except:
            return ["my XRP is going crazy while line following what's wrong?"]
    
    def _ask(self, role: str, content: str):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", config=self.configs[role], contents=content)
        return response.parsed if role in ['grader', 'editor'] else response.text
    
    def evaluate(self, question: str, max_turns: int = 10) -> dict:
        expert_answer = self._ask('expert', question)
        conversation = question
        
        for turn in range(1, max_turns + 1):
            tutor_response = self._ask('tutor', conversation)
            conversation += f"\n\nTutor: {tutor_response}"
            
            student_response = self._ask('student', conversation)
            
            if "I'm satisfied with my care" in student_response:
                break
            conversation += f"\n\nStudent: {student_response}"
        
        evaluation = self._ask('grader', f"{conversation}\n\nEXPERT:\n{expert_answer}")
        
        self.feedback_history.append({
            'timestamp': datetime.now().isoformat(), 'question': question,
            'grade': evaluation.grade, 'score': evaluation.prompt_adherence_score,
            'improvements': evaluation.improvement_suggestions, 'turns': turn,
            'satisfied': "I'm satisfied with my care" in student_response
        })
        self._save_json("feedback_history.json", self.feedback_history)
        
        return {'evaluation': evaluation, 'turns': turn, 'satisfied': "I'm satisfied with my care" in student_response}
    
    def get_summary(self):
        if not self.feedback_history: return {'total': 0}
        
        improvements = [item for entry in self.feedback_history for item in entry['improvements']]
        
        return {
            'total': len(self.feedback_history),
            'avg_score': round(sum(e['score'] for e in self.feedback_history) / len(self.feedback_history), 1),
            'grades': {g: sum(1 for e in self.feedback_history if e['grade'] == g) for g in set(e['grade'] for e in self.feedback_history)},
            'top_issues': sorted({i: improvements.count(i) for i in set(improvements)}.items(), 
                               key=lambda x: x[1], reverse=True)[:3]
        }
    
    def suggest_improvements(self):
        if len(self.feedback_history) < 2: return None
        
        summary = self.get_summary()
        prompt = pathlib.Path('prompts/tutor_prompt.txt').read_text()
        
        context = f"""CURRENT PROMPT:\n{prompt}\n
ANALYSIS: {summary['total']} evals, avg {summary['avg_score']}/10, grades {summary['grades']}
TOP ISSUES: {[f"{imp} ({count}x)" for imp, count in summary['top_issues']]}

Suggest specific prompt improvements."""
        
        return self._ask('editor', context)
    
    def apply_improvements(self):
        suggestion = self.suggest_improvements()
        if not suggestion: return False
        
        # Format and save updated prompt
        text = suggestion.updated_prompt.strip().strip('"""').strip()
        formatted = f'"""\n{text}\n"""'
        formatted = re.sub(r'\n\n\n+', '\n\n', formatted.replace('**', '\n**'))
        formatted = formatted.replace('"""\n\n**', '"""\n**')
        
        pathlib.Path('prompts/tutor_prompt.txt').write_text(formatted)
        print(f"Prompt updated: {', '.join(suggestion.changes_made)}")
        return True
    
    def clear_history(self):
        self.feedback_history = []
        self._save_json("feedback_history.json", [])
    
    def evaluate_batch(self, n=5, max_turns=10):
        questions = random.sample(self.questions, min(n, len(self.questions)))
        results = []
        
        for i, question in enumerate(questions, 1):
            print(f"Question {i}/{len(questions)}: {question[:60]}...")
            results.append(self.evaluate(question, max_turns))
        
        return results


def main():
    evaluator = XRPEvaluator()
    results = evaluator.evaluate_batch()
    
    scores = [r['evaluation'].prompt_adherence_score for r in results]
    grades = [r['evaluation'].grade for r in results]
    
    print(f"\nResults: {len(results)} questions, avg {sum(scores)/len(scores):.1f}/10")
    print(f"Grades: {dict(zip(*zip(*[(g, grades.count(g)) for g in set(grades)])))} ")
    print(f"Satisfied: {sum(r['satisfied'] for r in results)}/{len(results)}")
    
    summary = evaluator.get_summary()
    if summary['total'] > 1:
        print(f"Total: {summary['total']} evals, avg {summary['avg_score']}/10")
        
        if input("\nApply improvements? (y/n): ").lower() == 'y':
            evaluator.apply_improvements()
        
        if input("Clear history? (y/n): ").lower() == 'y':
            evaluator.clear_history()


if __name__ == "__main__":
    main()