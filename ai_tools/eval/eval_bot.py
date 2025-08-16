import os
import pathlib
import google.generativeai
from dotenv import load_dotenv
import pickle
import gzip
import random
import time # Import time for delays
from link_checker import LinkChecker
from prompt_manager import PromptManager
from prompt_editor import PromptEditor, FeedbackSummary

# Global counter for tracking skipped responses due to filtering/errors
SKIPPED_RESPONSE_COUNTER = {
    'tutor_bot': 0,
    'student_impersonator': 0,
    'expert_grader': 0
}


def setup_gemini_client():
    load_dotenv()
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        print("GOOGLE_AI_API_KEY not found in environment variables!")
        print("Make sure you have set up your API key in the .env file")
        return None
    try:
        google.generativeai.configure(api_key=api_key)
        return google.generativeai
    except Exception as e:
        print(f"Error setting up Gemini client: {e}")
        return None

# Student Impersonator Model
class StudentImpersonator:
    def __init__(self, all_faq_questions: list):
        self.faq_questions = all_faq_questions
        self.conversation_turns = [] # Stores (student_q, tutor_a) for internal use
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-pro")
            self.chat = self.model.start_chat()
        else:
            self.model = None
            self.chat = None

    def ask_question(self, last_tutor_response: str = None):
        global SKIPPED_RESPONSE_COUNTER
        if not self.model or not self.chat:
            return "Student impersonator not initialized due to API error."

        if not self.conversation_turns:
            # First question - choose a random one from FAQ
            question = random.choice(self.faq_questions)
            self.conversation_turns.append((question, None)) # Store the question, tutor response will be added later
            return question
        else:
            # Update the last turn with the tutor's response before generating a new question
            if last_tutor_response:
                last_q, _ = self.conversation_turns[-1]
                self.conversation_turns[-1] = (last_q, last_tutor_response)

            # Check for satisfaction - be inquisitive and focused
            satisfaction_prompt = f"""You are a curious student learning XRP robotics. You have a specific question you're trying to get answered. You just received this response from your tutor:

Tutor's Response: {last_tutor_response}

EVALUATION: Consider your original question and learning goal. Ask yourself:
1. Has this response helped you understand how to solve your original problem?
2. Do you feel like you're making progress toward your specific goal?
3. Are you getting the information you need, even if it's through guided discovery?

You're satisfied when you feel you understand the approach to solve your original problem, whether through direct answers, helpful guidance, or step-by-step learning. You're willing to engage with questions and hints if they're clearly leading you toward your goal.

Answer 'YES' if you feel you have fully gotten the help you need for your original question. Answer 'NO' if you feel the conversation has gotten off-track from your goal.

Your answer:"""
            
            try:
                satisfaction_response = self.chat.send_message(satisfaction_prompt)
                
                # Check if response has valid text content
                if not satisfaction_response.candidates or not satisfaction_response.candidates[0].content.parts:
                    SKIPPED_RESPONSE_COUNTER['student_impersonator'] += 1
                    # Continue to generate a new question instead of ending conversation
                else:
                    if "YES" in satisfaction_response.text.upper():
                        self.conversation_turns.append(("I'm satisfied with my care", None))
                        return "I'm satisfied with my care"
            except Exception as e:
                SKIPPED_RESPONSE_COUNTER['student_impersonator'] += 1

            conversation_context = ""
            for q, a in self.conversation_turns:
                conversation_context += f"Student: {q}\n"
                if a:
                    conversation_context += f"Tutor: {a}\n"

            prompt = f"""You are an inquisitive student learning XRP robotics. You're engaged in the conversation and want to understand your original question thoroughly. Based on the previous conversation, continue exploring your topic while staying focused on your original goal.

Previous Conversation:
{conversation_context}

STAY FOCUSED AND INQUISITIVE:
- Build on what the tutor has shared with thoughtful follow-up questions
- If they gave you guidance, ask for clarification or next steps
- If they asked you questions, engage with them but relate back to your goal
- Show you're thinking about their suggestions and want to understand better
- Stay curious about the specific problem you originally asked about
- Ask for elaboration on points that will help you solve your original question

Your next thoughtful question that shows you're engaged and working toward understanding your original problem:"""

            try:
                response = self.chat.send_message(prompt)
                
                # Check if response has valid text content
                if not response.candidates or not response.candidates[0].content.parts:
                    SKIPPED_RESPONSE_COUNTER['student_impersonator'] += 1
                    return "Can you explain that further?" # Fallback generic question
                
                generated_question = response.text.strip()
                self.conversation_turns.append((generated_question, None)) # Store the new question
                return generated_question
            except Exception as e:
                SKIPPED_RESPONSE_COUNTER['student_impersonator'] += 1
                return "Can you explain that further?" # Fallback generic question

    def _format_faq_for_prompt(self):
        return "\n".join([f"- {q}" for q in self.faq_questions])

# Tutor Bot Model with Documentation Context
class TutorBot:
    def __init__(self, prompt_file: str = "tutor_prompt.txt", documentation_file: str = "combined_documentation.md"):
        self.prompt_manager = PromptManager()
        self.prompt_file = prompt_file
        self.documentation_file = documentation_file
        self.contextual_prompt = self._load_prompt()
        self.documentation_context = self._load_documentation()
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-pro")
            self.chat = None # Tutor bot will not use a persistent chat history for its main prompt
        else:
            self.model = None
            self.chat = None

    def _load_prompt(self) -> str:
        """Load prompt from file"""
        try:
            return self.prompt_manager.load_prompt(self.prompt_file)
        except FileNotFoundError:
            print(f"Warning: Prompt file '{self.prompt_file}' not found. Using fallback prompt.")
            return "You are a helpful programming tutor for XRP robotics."
        except Exception as e:
            print(f"Error loading prompt: {e}. Using fallback prompt.")
            return "You are a helpful programming tutor for XRP robotics."
    
    def _load_documentation(self) -> str:
        """Load combined documentation for context"""
        try:
            doc_path = os.path.join(os.path.dirname(__file__), self.documentation_file)
            with open(doc_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Warning: Documentation file '{self.documentation_file}' not found.")
            return ""
        except Exception as e:
            print(f"Error loading documentation: {e}")
            return ""
    
    def reload_prompt(self):
        """Reload prompt from file (useful after PromptEditor makes changes)"""
        self.contextual_prompt = self._load_prompt()

    def answer_question(self, question: str):
        global SKIPPED_RESPONSE_COUNTER
        if self.model:
            # Combine prompt + documentation + question
            full_context = f"""{self.contextual_prompt}

**AVAILABLE XRP DOCUMENTATION:**
{self.documentation_context}

**STUDENT'S QUESTION:**
{question}"""
            
            try:
                response = self.model.generate_content(full_context)
                
                # Check if response has valid text content
                if not response.candidates or not response.candidates[0].content.parts:
                    SKIPPED_RESPONSE_COUNTER['tutor_bot'] += 1
                    return None  # Signal to skip this Q&A pair
                
                return response.text
            except Exception as e:
                SKIPPED_RESPONSE_COUNTER['tutor_bot'] += 1
                return None  # Signal to skip this Q&A pair
        else:
            return "Tutor bot not initialized due to API error."

# Expert Grader Model
class ExpertGrader:
    def __init__(self, answers_data: dict):
        self.answers = answers_data
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-pro")
            self.chat = self.model.start_chat()
        else:
            self.model = None
            self.chat = None

    def _load_answers(self, file_path: str):
        # This method is now effectively deprecated as answers are passed directly
        # Keeping it for now but it won't be called from __init__
        try:
            with gzip.open(file_path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print(f"Warning: Answers file '{file_path}' not found.")
            return {}
        except Exception as e:
            print(f"Error loading answers file: {e}")
            return {}

    def grade_conversation(self, student_question: str, tutor_response: str, link_feedback: str = None):
        global SKIPPED_RESPONSE_COUNTER
        if not self.model or not self.chat:
            return "Expert grader not initialized due to API error."

        correct_answer = self.answers.get(student_question, "No expert answer available for this question.")

        grading_prompt = f"""You are an expert grader evaluating how well a tutor bot follows its educational prompt guidelines. The tutor should adapt its response style based on the type of question asked.

**GRADING STANDARDS:**

**EXCELLENT (A):**
- Correctly identifies question type (quick clarification vs. complex problem-solving)
- For QUICK questions: Provides direct, concise answers with brief explanations
- For COMPLEX questions: Uses appropriate Socratic method and graduated response levels
- Follows the 5-level framework (Hint → Concept → Pseudocode → Example → Solution) when appropriate
- Encourages code generation and hands-on learning
- References documentation appropriately with valid, working links

**GOOD (B):**
- Generally matches response style to question type with minor misalignment
- Uses most prompt guidelines effectively
- Some progress toward learning objectives

**AVERAGE (C):**
- Mixed adherence to prompt guidelines
- Sometimes over-complicates simple questions or over-simplifies complex ones
- Partial use of educational framework

**POOR (D-F):**
- Fails to match response style to question type
- Ignores prompt guidelines (e.g., uses Socratic method for simple clarification questions)
- No clear educational strategy or progression

**Evaluation Context:**
Student Question: {student_question}
Tutor Response: {tutor_response}
Expert Answer: {correct_answer}

**Link Checker Feedback:**
{link_feedback if link_feedback else "No link issues found."}

**Key Questions:** 
1. Did the tutor correctly assess the question type (quick vs. complex)?
2. Did the tutor follow its prompt guidelines appropriately for that question type?
3. Was the response level (Hint/Concept/Pseudocode/Example/Solution) appropriate?
4. Did the tutor handle documentation links correctly (no broken links, appropriate references)?

Grade: 
Explanation (focus on prompt adherence and link quality):"""

        try:
            response = self.chat.send_message(grading_prompt)
            
            # Check if response has valid text content
            if not response.candidates or not response.candidates[0].content.parts:
                SKIPPED_RESPONSE_COUNTER['expert_grader'] += 1
                return "Grade: N/A\nExplanation: Response was filtered due to content policy."
            
            return response.text
        except Exception as e:
            SKIPPED_RESPONSE_COUNTER['expert_grader'] += 1
            return "Grade: N/A\nExplanation: Error occurred during grading."


def load_answers_from_pkl(file_path="answers.pkl.gz"):
    try:
        with gzip.open(file_path, 'rb') as f:
            answers = pickle.load(f)
        questions = list(answers.keys())
        return questions, answers
    except FileNotFoundError:
        print(f"Error: Answers file '{file_path}' not found. Please ensure the file exists.")
        return [], {}
    except Exception as e:
        print(f"Error loading answers file: {e}")
        return [], {}

def run_single_conversation(student, tutor, grader, link_checker, qa_index, total_questions, initial_question=None):
    """Run a single multi-turn conversation until student satisfaction"""
    print(f"{qa_index + 1}: {initial_question}")
    
    conversation_history = []
    total_tokens = 0
    turn_count = 0
    current_student_question = None
    prev_tutor_response = None

    while True:
        turn_count += 1

        # Student asks question
        current_student_question = student.ask_question(last_tutor_response=prev_tutor_response)

        if current_student_question == "I'm satisfied with my care":
            break

        # Tutor responds
        tutor_response = tutor.answer_question(current_student_question)

        # If tutor response is None, skip this Q&A pair
        if tutor_response is None:
            break
        
        # Check tutor response with LinkChecker
        link_check_results = link_checker.check_tutor_response(tutor_response)
        link_feedback = link_checker.generate_feedback_report(link_check_results)
        
        conversation_history.append({
            "student_question": current_student_question,
            "tutor_response": tutor_response,
            "link_check_results": link_check_results,
            "link_feedback": link_feedback
        })
        
        prev_tutor_response = tutor_response # Update for the next student turn

    # Grade the conversation (using the last turn for now)
    grade_text = ""
    link_score = 1.0
    if conversation_history:
        last_turn = conversation_history[-1]
        # If the last student question was the satisfaction message, use the previous turn for grading if available
        if last_turn["student_question"] == "I'm satisfied with my care" and len(conversation_history) > 1:
            last_turn = conversation_history[-2]

        grade_text = grader.grade_conversation(
            last_turn["student_question"], 
            last_turn["tutor_response"],
            last_turn["link_feedback"]
        )
        link_score = last_turn["link_check_results"]["overall_score"]
    
    return conversation_history, grade_text, link_score

def extract_grade_from_text(grade_text: str) -> str:
    """Extract letter grade from grader response"""
    lines = grade_text.split('\n')
    for line in lines:
        # Handle both "Grade:" and "**Grade:**" formats
        if 'Grade:' in line:
            # Remove markdown formatting and extract grade
            grade_part = line.split('Grade:')[1].strip()
            if grade_part:
                # Take first word and remove any parentheses (e.g., "A (Excellent)" -> "A")
                grade = grade_part.split()[0].replace('(', '').replace(')', '')
                return grade
    return "N/A"

def extract_issues_from_grade(grade_text: str) -> list:
    """Extract issues from grader feedback"""
    issues = []
    if any(word in grade_text.lower() for word in ['poor', 'lacks', 'missing', 'ineffective', 'doesn\'t']):
        # Simple heuristic to extract negative feedback
        sentences = grade_text.split('.')
        for sentence in sentences:
            if any(word in sentence.lower() for word in ['poor', 'lacks', 'missing', 'ineffective', 'doesn\'t']):
                issues.append(sentence.strip())
    return issues

def main():
    # Configuration
    NUM_QUESTIONS = 5
    
    all_faq_questions, all_answers = load_answers_from_pkl()
    if not all_faq_questions:
        print("No questions loaded from answers.pkl.gz. Exiting.")
        return

    # Random sample of questions
    limited_questions = random.sample(all_faq_questions, min(NUM_QUESTIONS, len(all_faq_questions)))
    
    # Initialize all agents
    tutor = TutorBot()
    grader = ExpertGrader(answers_data=all_answers)
    link_checker = LinkChecker()
    
    # Track overall results and failed questions
    all_results = []
    failed_questions = []
    conversation_count = 0
    
    # Iterate through limited Q/A pairs
    for qa_index, initial_question in enumerate(limited_questions):
        conversation_count += 1
        
        # Create a new student impersonator for each conversation
        # Starting with the specific FAQ question
        student = StudentImpersonator([initial_question])
        
        # Run single conversation
        conversation_history, grade_text, link_score = run_single_conversation(
            student, tutor, grader, link_checker, qa_index, len(limited_questions), initial_question
        )
        
        # Track failed questions (those with no conversation history due to skipping)
        if not conversation_history:
            failed_questions.append(initial_question)
        
        # Extract grader information
        letter_grade = extract_grade_from_text(grade_text)
        grader_issues = extract_issues_from_grade(grade_text)
        link_issues = conversation_history[-1]["link_check_results"]["issues_found"] if conversation_history else []
        
        # Create feedback summary for PromptEditor
        # feedback_summary = FeedbackSummary(
        #     grader_grade=letter_grade,
        #     grader_issues=grader_issues,
        #     link_issues=link_issues,
        #     overall_score=link_score,
        #     conversation_turn=conversation_count
        # )
        
        # Run PromptEditor to improve prompt
        # editor_results = prompt_editor.process_feedback_and_improve(feedback_summary)
        
        # if editor_results["prompt_updated"]:
        #     # Reload the tutor's prompt
        #     tutor.reload_prompt()
        
        # Store results
        all_results.append({
            "qa_index": qa_index,
            "initial_question": initial_question,
            "conversation_turns": len(conversation_history),
            "grade": letter_grade,
            "link_score": link_score,
            # "prompt_updated": editor_results["prompt_updated"],
            # "applied_modifications": editor_results["applied_modifications"]
        })
    
    # Final summary
    print(f"\n{'='*60}")
    print("FINAL EVALUATION SUMMARY")
    print(f"{'='*60}")
    print(f"Total Conversations: {len(all_results)}")
    print(f"Average Link Score: {sum(r['link_score'] for r in all_results) / len(all_results):.2f}")
    # print(f"Prompt Updates: {sum(1 for r in all_results if r['prompt_updated'])}")
    # print(f"Total Modifications Applied: {sum(r['applied_modifications'] for r in all_results)}")
    
    # Grade distribution
    grades = [r['grade'] for r in all_results]
    grade_counts = {grade: grades.count(grade) for grade in set(grades)}
    print(f"Grade Distribution: {grade_counts}")
    
    # Average conversation length
    avg_turns = sum(r['conversation_turns'] for r in all_results) / len(all_results)
    print(f"Average Conversation Length: {avg_turns:.1f} turns")
    
    # Skipped response statistics
    global SKIPPED_RESPONSE_COUNTER
    total_skipped = sum(SKIPPED_RESPONSE_COUNTER.values())
    print(f"\n{'='*60}")
    print("SKIPPED RESPONSE STATISTICS")
    print(f"{'='*60}")
    print(f"Total Skipped Responses (due to errors/filtering): {total_skipped}")
    print(f"  - TutorBot: {SKIPPED_RESPONSE_COUNTER['tutor_bot']}")
    print(f"  - StudentImpersonator: {SKIPPED_RESPONSE_COUNTER['student_impersonator']}")
    print(f"  - ExpertGrader: {SKIPPED_RESPONSE_COUNTER['expert_grader']}")
    if total_skipped > 0:
        print(f"Skip Rate: {(total_skipped / len(all_results)) * 100:.2f}%")
    
    # Save failed questions to file
    if failed_questions:
        with open('failed_questions.txt', 'w', encoding='utf-8') as f:
            f.write("Failed Questions (could not be processed):\n")
            f.write("=" * 50 + "\n\n")
            for i, question in enumerate(failed_questions, 1):
                f.write(f"{i}. {question}\n")
        print(f"Saved {len(failed_questions)} failed questions to 'failed_questions.txt'")
    
    print(f"\nEvaluation complete! Results show tutor bot performance across {NUM_QUESTIONS} FAQ questions.")

if __name__ == "__main__":
    main() 