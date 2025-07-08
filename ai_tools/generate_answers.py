import os
import re
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from XRPTutor import XRPTutor

# Path to the generated FAQs directory
FAQ_DIR = "../generated_faqs"

# Helper to extract questions from a FAQ markdown file
def extract_questions_from_faq(faq_path, max_questions=2):
    questions = []
    numbered_q_pattern = re.compile(r"^\d+\.\s+(.*)")
    with open(faq_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            match = numbered_q_pattern.match(line)
            if match:
                q = match.group(1).strip()
                questions.append(q)
                if len(questions) >= max_questions:
                    break
    return questions

def main():
    tutor = XRPTutor()
    # Get the list of FAQ files in the directory
    faq_files = sorted([f for f in os.listdir(FAQ_DIR) if f.endswith('.md')])
    if not faq_files:
        print("No FAQ files found.")
        return
    for faq_file in faq_files:
        faq_path = os.path.join(FAQ_DIR, faq_file)
        questions = extract_questions_from_faq(faq_path, max_questions=2)
        print(f"\n==============================\nPrompts for file: {faq_file}\n==============================")
        if not questions:
            print(f"No questions found in {faq_file}")
            continue
        for i, question in enumerate(questions, 1):
            print(f"\n---\nPrompt for FAQ Question {i}:")
            prompt = tutor.generate_response_prompt(question)

if __name__ == "__main__":
    main() 