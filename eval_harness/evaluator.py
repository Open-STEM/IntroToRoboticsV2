from google import genai
from google.genai import types
import pathlib, json, random, re, os
from pydantic import BaseModel
from datetime import datetime
from dotenv import load_dotenv

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

class HarnessEvaluator:
    def __init__(self, prompt_dir: str, curriculum_path: str, feedback_history_path: str = "feedback_history.json"):
        self.prompt_dir = pathlib.Path(prompt_dir)
        self.curriculum_path = pathlib.Path(curriculum_path)
        self.feedback_history_path = pathlib.Path(feedback_history_path)
        self.client = self._setup_gemini_client()
        self.feedback_history = self._load_json(self.feedback_history_path, [])
        
        self.prompts = self._load_prompts()
        self.curriculum = self._load_curriculum()
        self.configs = self._setup_configs()

    def _setup_gemini_client(self):
        api_key = os.getenv('GOOGLE_AI_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_AI_API_KEY not found in environment variables! Please set it in your .env file or pass it directly.")
        return genai.Client(api_key=api_key)

    def _load_json(self, file_path: pathlib.Path, default):
        try:
            return json.loads(file_path.read_text())
        except (FileNotFoundError, json.JSONDecodeError):
            return default
    
    def _save_json(self, file_path: pathlib.Path, data):
        file_path.write_text(json.dumps(data, indent=2))

    def _load_prompts(self):
        prompts = {}
        for f in self.prompt_dir.glob('*_prompt.txt'):
            role = f.stem.split('_')[0]
            prompts[role] = f.read_text()
        return prompts

    def _load_curriculum(self):
        if not self.curriculum_path.exists():
            raise FileNotFoundError(f"Curriculum documentation not found: {self.curriculum_path}")
        return self.curriculum_path.read_text()

    def _setup_configs(self):
        configs = {}
        for role, prompt_text in self.prompts.items():
            system_instruction = prompt_text
            if role in ['expert', 'tutor']:
                system_instruction = f"{prompt_text}\n\nDOCS:\n{self.curriculum}"
            
            response_mime_type = None
            response_schema = None
            if role == 'grader':
                response_mime_type = "application/json"
                response_schema = GraderEvaluation
            elif role == 'editor':
                response_mime_type = "application/json"
                response_schema = PromptEditSuggestion
            
            configs[role] = types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type=response_mime_type,
                response_schema=response_schema
            )
        return configs
    
    def _ask(self, role: str, content: str, model_name: str = "gemini-2.5-flash"):
        response = self.client.models.generate_content(
            model=model_name, config=self.configs[role], contents=content)
        return response.parsed if role in ['grader', 'editor'] else response.text
    
    def evaluate_conversation(self, question: str, max_turns: int = 10) -> dict:
        expert_answer = self._ask('expert', question)
        conversation = question
        
        satisfied = False
        for turn in range(1, max_turns + 1):
            tutor_response = self._ask('tutor', conversation)
            conversation += f"\nTutor: {tutor_response}"
            
            student_response = self._ask('student', conversation)
            
            if "I'm satisfied with my care" in student_response:
                satisfied = True
                break
            conversation += f"\n\nStudent: {student_response}"
        
        evaluation = self._ask('grader', f"{conversation}\n\nEXPERT:\n{expert_answer}")
        
        self.feedback_history.append({
            'timestamp': datetime.now().isoformat(), 'question': question,
            'grade': evaluation.grade, 'score': evaluation.prompt_adherence_score,
            'improvements': evaluation.improvement_suggestions, 'turns': turn,
            'satisfied': satisfied
        })
        self._save_json(self.feedback_history_path, self.feedback_history)
        
        return {'evaluation': evaluation, 'turns': turn, 'satisfied': satisfied}
    
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
        tutor_prompt = self.prompts.get('tutor', '') # Get current tutor prompt
        
        context = f"""CURRENT TUTOR PROMPT:
{tutor_prompt}

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
        
        tutor_prompt_path = self.prompt_dir / "tutor_prompt.txt"
        tutor_prompt_path.write_text(formatted)
        print(f"Prompt updated: {', '.join(suggestion.changes_made)}")
        
        # Reload prompts and configs after applying improvements
        self.prompts = self._load_prompts()
        self.configs = self._setup_configs()
        return True
    
    def clear_history(self):
        self.feedback_history = []
        self._save_json(self.feedback_history_path, self.feedback_history)
        print(f"Feedback history cleared from {self.feedback_history_path}")

if __name__ == "__main__":
    # Example usage:
    # This assumes curriculum.md is in ai_tools/ and prompts/ is in eval_harness/
    evaluator = HarnessEvaluator(
        prompt_dir="prompts",
        curriculum_path="combined_documentation.md",
        feedback_history_path="feedback_history.json" # Relative to eval_harness/
    )

    # Example questions (in a real scenario, these would come from FAQGenerator)
    sample_questions = [
        "How do I make the robot drive straight for 20 cm?",
        "What's the difference between set_effort and set_speed?",
        "Why does the IMU need to be calibrated?"
    ]

    print("Running sample evaluations...")
    for i, q in enumerate(sample_questions):
        print(f"\n--- Evaluating Question {i+1}: {q[:50]}... ---")
        result = evaluator.evaluate_conversation(q)
        print(f"  Grade: {result['evaluation'].grade}, Score: {result['evaluation'].prompt_adherence_score}")
        print(f"  Satisfied: {result['satisfied']}, Turns: {result['turns']}")
    
    print("\n--- Summary ---")
    summary = evaluator.get_summary()
    print(summary)

    # Example of applying improvements (requires sufficient history)
    # if summary['total'] >= 2:
    #     if input("\nApply improvements? (y/n): ").lower() == 'y':
    #         evaluator.apply_improvements()

    # if input("Clear history? (y/n): ").lower() == 'y':
    #     evaluator.clear_history()
