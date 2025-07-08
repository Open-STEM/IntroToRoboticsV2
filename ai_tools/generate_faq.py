#!/usr/bin/env python3
"""
Script to generate FAQ questions using Gemini AI for robotics course lessons.
Uses the combined documentation as context and processes lesson files.
"""

import os
import pathlib
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from identify_lesson_files import identify_lesson_files

# Load environment variables from .env file
load_dotenv()

def setup_gemini_client():
    """Setup and return a Gemini AI client."""
    try:
        api_key = os.getenv('GOOGLE_AI_API_KEY')
        if not api_key:
            print("GOOGLE_AI_API_KEY not found in environment variables!")
            print("Make sure you have set up your API key in the .env file")
            return None
        
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f"Error setting up Gemini client: {e}")
        print("Make sure you have set up your API key properly.")
        return None

def load_documentation_context():
    """Load the combined documentation as a Part object for context."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    doc_path = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'combined_documentation.md')) # Corrected path using script_dir
    
    print(f"Attempting to load documentation from: {doc_path.absolute()}") # Debugging print
    if not doc_path.exists():
        print(f"Combined documentation file not found at {doc_path}")
        return None
    
    try:
        print("Loading combined documentation as context...")
        doc_part = types.Part.from_bytes(
            data=doc_path.read_bytes(),
            mime_type='text/markdown'
        )
        print(f"Documentation loaded successfully: {doc_path.name}")
        return doc_part
    except Exception as e:
        print(f"Error loading documentation: {e}")
        return None

def get_available_lessons():
    """Get the list of lesson files by importing the identification module."""
    try:
        # Adjusted call to the correct function name
        lesson_results = identify_lesson_files()
        return [{"file_path": p, "lesson_score": 0, "word_count": 0} for p in lesson_results] # Returning a list of dictionaries to match expected format
    except Exception as e:
        print(f"Error getting lesson files: {e}")
        return []

def read_lesson_content(lesson_file_path):
    """
    Read the content of a lesson file.
    """
    try:
        with open(lesson_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading lesson file {lesson_file_path}: {e}")
        return None

def generate_faq_for_lesson(client, documentation_part, lesson_content, lesson_name):
    """
    Generate FAQ questions for a specific lesson using Gemini AI.
    """
    
    system_instruction = """You are an experienced robotics educator who helps middle and high school students learn robotics concepts. Your task is to generate realistic FAQ questions that represent a wide variety of student types and teaching scenarios.

Based on the provided lesson content and the comprehensive robotics course documentation as context, generate FAQ questions from these different perspectives:

**STUDENT PERSONAS TO REPRESENT:**
1. **Curious Learner** – asks "why" and "how" questions, genuinely wants to understand underlying concepts
2. **Confused Student** – lacks basic understanding, needs fundamental concepts clarified
3. **Rushed Crammer** – wants quick, direct answers without deep explanation
4. **Step-by-Step Seeker** – requests guided help and detailed procedures
5. **Skeptical Challenger** – questions or doubts explanations, needs convincing
6. **Advanced Explorer** – dives deep or connects topics across lessons
7. **Forgetful Reviewer** – struggles with recall, asks about previously covered material
8. **Overconfident Guesser** – assumes answers or makes confident but often wrong statements
9. **Minimal Responder** – gives short or vague replies when asked to explain their thinking
10. **Misconception Holder** – believes common myths or errors about robotics/programming

**GENERATE 50 QUESTIONS TOTAL (5 from each persona):**
- 5 Curious Learner questions (asking "why" and "how" with genuine interest)
- 5 Confused Student questions (showing lack of basic understanding)
- 5 Rushed Crammer questions (seeking quick, direct answers)
- 5 Step-by-Step Seeker questions (requesting detailed guidance)
- 5 Skeptical Challenger questions (doubting or challenging explanations)
- 5 Advanced Explorer questions (diving deep or connecting across topics)
- 5 Forgetful Reviewer questions (about recall and retention)
- 5 Overconfident Guesser questions (confident but incorrect assumptions)
- 5 Minimal Responder questions (short, vague questions)
- 5 Misconception Holder questions (revealing common myths or errors)

**FORMAT:** Present all 50 questions as one continuous numbered list (1-50) without separating by persona type.

Make each question sound authentic to how that specific persona would actually communicate. Mix the personas throughout the list so it's not obvious which is which - this simulates a real classroom where different types of students ask questions randomly.

Output ONLY the numbered list of 50 questions. No headers, no explanations, no persona labels."""

    prompt = f"""
Generate FAQ questions for: {lesson_name}

Lesson Content:
{lesson_content}

Create questions that sound like each persona would actually ask them. Keep the format clean with just the section headers and numbered question lists.
"""

    try:
        print(f"Generating FAQ for lesson: {lesson_name}")
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            ),
            contents=[documentation_part, prompt]
        )
        
        return response.text
    except Exception as e:
        print(f"Error generating FAQ: {e}")
        return None

def create_master_faq(all_faq_contents, output_filename="faq.txt"):
    """
    Create a master FAQ file by concatenating all generated FAQ contents.
    """
    # Output file will be in the current working directory
    filepath = output_filename
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("XRP Robotics Course Combined FAQ\n\n")
            for faq_content in all_faq_contents:
                f.write(faq_content)
                f.write("\n\n") # Add a separator between different FAQ sets
        
        print(f"Master FAQ saved to: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error creating master FAQ: {e}")
        return None

def save_faq(lesson_name, faq_content, output_dir="../generated_faqs"):
    """Save the generated FAQ to a clean, simple format."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a safe filename from the lesson name
    safe_name = lesson_name.replace('/', '_').replace(' ', '_').replace('.rst', '')
    filename = f"{safe_name}_faq.md"
    filepath = os.path.join(output_dir, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write simple header
            f.write(f"# {lesson_name.replace('_', ' ').replace('.rst', '').title()}\n\n")
            
            # Write the FAQ content (which should already be organized by the AI)
            f.write(faq_content)
        
        print(f"FAQ saved to: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error saving FAQ: {e}")
        return None

def process_lesson(client, documentation_part, lesson_result):
    """
    Process a single lesson and generate FAQ for it.
    """
    lesson_path = lesson_result['file_path']
    lesson_name = os.path.basename(lesson_path)
    
    print(f"\nProcessing lesson: {lesson_name}")
    print(f"  Path: {lesson_path}")
    
    # Read lesson content
    lesson_content = read_lesson_content(lesson_path)
    if lesson_content is None:
        return None

    # Generate FAQ
    faq_content = generate_faq_for_lesson(client, documentation_part, lesson_content, lesson_name)
    if faq_content is None:
        return None

    return faq_content # Return raw FAQ content directly

def main(lesson_index=0, course_dir="../course", sample_size=None):
    """
    Main function to orchestrate FAQ generation.
    """
    client = setup_gemini_client()
    if client is None:
        return

    documentation_part = load_documentation_context()
    if documentation_part is None:
        return

    all_lessons = get_available_lessons()
    if not all_lessons:
        print("No lessons found to process.")
        return

    print(f"Found {len(all_lessons)} lesson files.")

    lessons_to_process = []
    if sample_size is not None:
        lessons_to_process = all_lessons[:sample_size]
    else:
        lessons_to_process = all_lessons # Process all lessons by default

    all_faq_results = []
    for lesson_result in lessons_to_process:
        faq_content = process_lesson(client, documentation_part, lesson_result)
        if faq_content:
            all_faq_results.append(faq_content)

    if all_faq_results:
        create_master_faq(all_faq_results) # Call without output_dir
        print("\nFAQ generation complete!")
    else:
        print("\nNo FAQs were generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate FAQ questions for XRP robotics lessons.")
    parser.add_argument('--lesson_index', type=int, default=0,
                        help='Index of the lesson to process (default: 0 for the first lesson).')
    parser.add_argument('--course_dir', type=str, default="../course",
                        help='Path to the course directory (default: ../course).')
    parser.add_argument('--sample_size', type=int, default=None,
                        help='Number of lessons to process (default: all).')

    args = parser.parse_args()
    main(lesson_index=args.lesson_index, course_dir=args.course_dir, sample_size=args.sample_size)