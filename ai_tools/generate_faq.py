#!/usr/bin/env python3
"""Generate FAQ questions using Gemini AI for robotics course lessons."""

import os
import pathlib
import glob
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def setup_gemini_client():
    """Setup and return a Gemini AI client."""
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_AI_API_KEY not found in environment variables!")
    return genai.Client(api_key=api_key)

def load_documentation():
    """Load the combined documentation."""
    doc_path = pathlib.Path("combined_documentation.md")
    if not doc_path.exists():
        raise FileNotFoundError(f"Documentation not found: {doc_path}")
    return doc_path.read_text()

def get_lesson_files():
    """Get all .rst lesson files from the course directory."""
    course_dir = pathlib.Path("../course")
    return list(course_dir.rglob("*.rst"))

def generate_questions(client, documentation, lesson_files):
    """Generate FAQ questions for all lessons."""
    
    # Combine all lesson content
    all_content = []
    for lesson_file in lesson_files:
        try:
            content = lesson_file.read_text()
            all_content.append(f"=== {lesson_file.name} ===\n{content}\n")
        except Exception as e:
            print(f"Error reading {lesson_file}: {e}")
    
    combined_lessons = "\n".join(all_content)
    
    system_instruction = """You are a robotics educator. Generate concise, realistic FAQ questions that students would ask about XRP robotics lessons.

Create questions that are:
- Direct and conversational (like real student questions)
- Mix of difficulty levels (basic to advanced)
- Cover different learning styles and personalities
- Range from simple clarifications to complex applications

Format: Just numbered questions (1. 2. 3. etc.) with no extra formatting."""

    prompt = f"""Based on this XRP robotics course content, generate 100 realistic student FAQ questions:

COURSE DOCUMENTATION:
{documentation}

LESSON CONTENT:
{combined_lessons}

Generate exactly 100 questions in this format:
1. [question]
2. [question]
...etc"""

    try:
        print("Generating FAQ questions...")
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=system_instruction),
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Error generating FAQ: {e}")
        return None

def main():
    """Generate FAQ questions for XRP robotics course."""
    try:
        client = setup_gemini_client()
        documentation = load_documentation()
        lesson_files = get_lesson_files()
        
        print(f"Found {len(lesson_files)} lesson files")
        
        questions = generate_questions(client, documentation, lesson_files)
        if questions:
            with open("faq.txt", "w") as f:
                f.write(questions)
            print("FAQ generated successfully and saved to faq.txt")
        else:
            print("Failed to generate FAQ")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()