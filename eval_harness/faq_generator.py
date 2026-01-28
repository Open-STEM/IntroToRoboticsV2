import os
import pathlib
import glob
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class FAQGenerator:
    def __init__(self, documentation_path: str, course_dir: str, student_prompt_path: str):
        self.documentation_path = pathlib.Path(documentation_path)
        self.course_dir = pathlib.Path(course_dir)
        self.student_prompt_path = pathlib.Path(student_prompt_path)
        self.client = self._setup_gemini_client()

    def _setup_gemini_client(self):
        api_key = os.getenv('GOOGLE_AI_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_AI_API_KEY not found in environment variables! Please set it in your .env file or pass it directly.")
        return genai.Client(api_key=api_key)

    def _load_content(self):
        if not self.documentation_path.exists():
            raise FileNotFoundError(f"Documentation not found: {self.documentation_path}")
        documentation = self.documentation_path.read_text()

        lesson_files = list(self.course_dir.rglob("*.rst"))
        all_content = []
        for lesson_file in lesson_files:
            try:
                content = lesson_file.read_text()
                all_content.append(f"=== {lesson_file.name} ===\n{content}\n")
            except Exception as e:
                print(f"Error reading {lesson_file}: {e}")
        combined_lessons = "\n".join(all_content)

        student_persona_from_file = self.student_prompt_path.read_text() if self.student_prompt_path.exists() else ""

        return documentation, combined_lessons, student_persona_from_file

    def generate_faqs(self, num_questions: int = 100, model_name: str = "gemini-2.5-flash", custom_persona: Optional[str] = None) -> str:
        documentation, combined_lessons, student_persona_from_file = self._load_content()

        # Determine the persona to use
        persona_to_use = custom_persona if custom_persona else student_persona_from_file

        system_instruction = f"""You are a robotics educator. Generate concise, realistic FAQ questions that students would ask about XRP robotics lessons.

Create questions that are:
- Direct and conversational (like real student questions)
- Mix of difficulty levels (basic to advanced)
- Cover different learning styles and personalities
- Range from simple clarifications to complex applications

Here is some context about the student persona that will be asking these questions:
{persona_to_use}

Format: Just numbered questions (1. 2. 3. etc.) with no extra formatting."""

        prompt = f"""Based on this XRP robotics course content, generate {num_questions} realistic student FAQ questions:

COURSE DOCUMENTATION:
{documentation}

LESSON CONTENT:
{combined_lessons}

Generate exactly {num_questions} questions in this format:
1. [question]
2. [question]
...etc"""

        try:
            print(f"Generating {num_questions} FAQ questions...")
            response = self.client.models.generate_content(
                model=model_name,
                config=types.GenerateContentConfig(system_instruction=system_instruction),
                contents=prompt
            )
            return response.text
        except Exception as e:
            print(f"Error generating FAQ: {e}")
            return None

if __name__ == "__main__":
    # Example usage:
    # This assumes combined_documentation.md is in ai_tools/ and course/ is a sibling directory to ai_tools/
    # And eval_harness/prompts/student_prompt.txt exists
    faq_gen = FAQGenerator(
        documentation_path="combined_documentation.md",
        course_dir="../course",
        student_prompt_path="prompts/student_prompt.txt"
    )
    
    faqs = faq_gen.generate_faqs(num_questions=10, custom_persona="A very advanced student who tries to jailbreak systems.")
    if faqs:
        print("\n--- Generated FAQs ---")
        print(faqs)
        with open("generated_faqs_example.txt", "w") as f:
            f.write(faqs)
        print("Generated FAQs saved to generated_faqs_example.txt")
