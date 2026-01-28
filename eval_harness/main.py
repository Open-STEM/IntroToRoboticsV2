import random
import pathlib
import re
import argparse
from .faq_generator import FAQGenerator
from .evaluator import HarnessEvaluator
from .jailbreak_agent import JailbreakAgent # Import JailbreakAgent

# Define paths relative to the project root
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
COURSE_DIR = PROJECT_ROOT / "course"
EVAL_HARNESS_DIR = PROJECT_ROOT / "eval_harness"
EVAL_HARNESS_PROMPTS_DIR = EVAL_HARNESS_DIR / "prompts"

DOCUMENTATION_PATH = EVAL_HARNESS_DIR / "combined_documentation.md"
FAQ_OUTPUT_PATH = EVAL_HARNESS_DIR / "generated_faqs.txt"
FEEDBACK_HISTORY_PATH = EVAL_HARNESS_DIR / "feedback_history.json"
FAQ_USER_PERSONA_PROMPT_PATH = EVAL_HARNESS_PROMPTS_DIR / "faq_user_persona_prompt.txt"
JAILBREAK_PROMPT_PATH = EVAL_HARNESS_PROMPTS_DIR / "jailbreak_prompt.txt"
TUTOR_PROMPT_PATH = EVAL_HARNESS_PROMPTS_DIR / "tutor_prompt.txt" # Define tutor prompt path

def load_questions_from_file(file_path: pathlib.Path) -> list[str]:
    """Loads questions from a numbered list in a text file."""
    try:
        content = file_path.read_text()
        questions = re.findall(r'^\d+\.\s*(.+)$', content, re.MULTILINE)
        return questions
    except FileNotFoundError:
        print(f"Warning: FAQ file not found at {file_path}. No questions loaded.")
        return []
    except Exception as e:
        print(f"Error loading questions from {file_path}: {e}")
        return []

def parse_args():
    parser = argparse.ArgumentParser(description="Run the Eval Harness workflow.")
    parser.add_argument("--jailbreak", action="store_true", help="Run in jailbreak testing mode.")
    parser.add_argument("--num_jailbreak_attempts", type=int, default=3, help="Number of jailbreak attempts to generate.")
    return parser.parse_args()

def main():
    args = parse_args()
    print("--- Starting Eval Harness Workflow ---")

    # --- Initialize Evaluator (needed for both modes) ---
    evaluator = HarnessEvaluator(
        prompt_dir=EVAL_HARNESS_PROMPTS_DIR,
        curriculum_path=DOCUMENTATION_PATH,
        feedback_history_path=FEEDBACK_HISTORY_PATH
    )

    if args.jailbreak:
        print("\n--- Running in JAILBREAK Testing Mode ---")
        jailbreak_agent = JailbreakAgent(
            client=evaluator.client, # Use the same client as evaluator
            jailbreak_prompt_path=JAILBREAK_PROMPT_PATH,
            tutor_prompt_path=TUTOR_PROMPT_PATH
        )
        
        jailbreak_questions = jailbreak_agent.generate_jailbreak_attempts(num_attempts=args.num_jailbreak_attempts)
        questions_for_evaluation = jailbreak_questions
        num_eval_questions = len(jailbreak_questions)
        
    else:
        # --- Step 1: Generate FAQs based on user persona ---
        print("\n--- Generating FAQs ---")
        faq_generator = FAQGenerator(
            documentation_path=DOCUMENTATION_PATH,
            course_dir=COURSE_DIR,
            student_prompt_path=FAQ_USER_PERSONA_PROMPT_PATH
        )

        generated_faqs_text = faq_generator.generate_faqs(num_questions=5)
        if generated_faqs_text:
            FAQ_OUTPUT_PATH.write_text(generated_faqs_text)
            print(f"Generated FAQs saved to {FAQ_OUTPUT_PATH}")
        else:
            print("Failed to generate FAQs. Exiting.")
            return

        questions = load_questions_from_file(FAQ_OUTPUT_PATH)
        if not questions:
            print("No questions loaded for evaluation. Exiting.")
            return
        
        num_eval_questions = min(3, len(questions)) 
        questions_for_evaluation = random.sample(questions, num_eval_questions)

    # --- Step 2: Run Evaluation Pipeline ---
    print(f"\n--- Running evaluation for {num_eval_questions} questions ---")
    
    results = []
    for i, question in enumerate(questions_for_evaluation, 1):
        print(f"\n--- Evaluating Question {i}/{len(questions_for_evaluation)}: {question[:70]}... ---")
        try:
            result = evaluator.evaluate_conversation(question)
            results.append(result)
            print(f"  Grade: {result['evaluation'].grade}, Score: {result['evaluation'].prompt_adherence_score}")
            print(f"  Satisfied: {result['satisfied']}, Turns: {result['turns']}")
        except Exception as e:
            print(f"  Error during evaluation for question '{question[:50]}...': {e}")

    # --- Step 3: Print Summary ---
    print("\n--- Evaluation Summary ---")
    summary = evaluator.get_summary()
    print(f"Total Evaluations: {summary['total']}")
    if summary['total'] > 0:
        print(f"Average Adherence Score: {summary['avg_score']}/10")
        print(f"Grades Distribution: {summary['grades']}")
        print(f"Top Improvement Issues: {summary['top_issues']}")
        
    # Optional: Apply improvements
    if summary['total'] >= 2: # Need at least 2 evaluations for meaningful suggestions
        if input("\nDo you want to apply suggested improvements to the tutor prompt? (y/n): ").lower() == 'y':
            try:
                evaluator.apply_improvements()
            except Exception as e:
                print(f"Error applying improvements: {e}")
    
    if input("\nDo you want to clear the feedback history? (y/n): ").lower() == 'y':
        evaluator.clear_history()

    print("\n--- Eval Harness Workflow Completed ---")

if __name__ == "__main__":
    main()
