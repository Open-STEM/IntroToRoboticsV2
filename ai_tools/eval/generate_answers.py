import os
import re
import sys
import pickle # Import the pickle module
import gzip
from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from XRPTutor import XRPTutor

# Path to the combined FAQ file
FAQ_FILE = "faq.txt"

# Helper to extract questions from the faq.txt file
def extract_questions_from_faq_txt(faq_path):
    questions = []
    # Regex to match numbered questions (e.g., "1. What's...")
    numbered_q_pattern = re.compile(r"^\d+\.\s+(.*)")
    with open(faq_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            match = numbered_q_pattern.match(line)
            if match:
                q = match.group(1).strip()
                questions.append(q)
    return questions

def main():
    tutor = XRPTutor()
    # Path to faq.txt relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    faq_file_path = os.path.join(script_dir, FAQ_FILE)

    questions = extract_questions_from_faq_txt(faq_file_path) # Get all questions
    if not questions:
        print(f"No questions found in {FAQ_FILE}")
        return

    expert_answers = {}
    for i, question in enumerate(questions, 1):
        print(f"\n==============================\nProcessing question {i}/{len(questions)}:\n{question}\n==============================")
        expert_answer = tutor.answer_question(question)
        print(f"Expert Answer:\n{expert_answer}\n")
        expert_answers[question] = expert_answer

    # Save all question-answer pairs as a dictionary to a compressed file using gzip
    compressed_pickle_file_path = os.path.join(script_dir, "answers.pkl.gz")
    with gzip.open(compressed_pickle_file_path, 'wb') as pkl_file:
        pickle.dump(expert_answers, pkl_file)
    print(f"All expert answers saved to {compressed_pickle_file_path}")

if __name__ == "__main__":
    main() 