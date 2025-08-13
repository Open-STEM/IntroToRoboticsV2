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
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-flash")
            self.chat = self.model.start_chat()
        else:
            self.model = None
            self.chat = None

    def ask_question(self, last_tutor_response: str = None):
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

            # Check for satisfaction
            satisfaction_prompt = f"""You are a student learning XRP robotics. You just received the following response from your tutor:

Tutor's Response: {last_tutor_response}

Based on this response and our previous conversation, are you satisfied with the explanation and ready to conclude this particular line of inquiry? Answer only with 'YES' or 'NO'.

Your answer:"""
            
            try:
                satisfaction_response = self.chat.send_message(satisfaction_prompt)
                time.sleep(1) # Add a small delay
                if "YES" in satisfaction_response.text.upper():
                    self.conversation_turns.append(("I'm satisfied with my care", None))
                    return "I'm satisfied with my care"
            except Exception as e:
                print(f"Error checking for student satisfaction: {e}")

            conversation_context = ""
            for q, a in self.conversation_turns:
                conversation_context += f"Student: {q}\n"
                if a:
                    conversation_context += f"Tutor: {a}\n"

            prompt = f"""You are a student learning XRP robotics. You are currently in a conversation with an AI tutor. Based on the previous conversation, ask a natural follow-up question, or if the topic seems concluded, ask a new, related question from the provided FAQ list. If you ask a new question, make it sound like a natural progression or a new thought.

Previous Conversation:
{conversation_context}

Available FAQ Questions (choose one if a new topic is desired, otherwise ask a follow-up):
{self._format_faq_for_prompt()}

Your next question to the tutor:"""

            try:
                response = self.chat.send_message(prompt)
                time.sleep(1) # Add a small delay
                generated_question = response.text.strip()
                self.conversation_turns.append((generated_question, None)) # Store the new question
                return generated_question
            except Exception as e:
                print(f"Error generating student question: {e}")
                return "Can you explain that further?" # Fallback generic question

    def _format_faq_for_prompt(self):
        return "\n".join([f"- {q}" for q in self.faq_questions])

# Tutor Bot Model
class TutorBot:
    def __init__(self, prompt_file: str = "tutor_prompt.txt"):
        self.prompt_manager = PromptManager()
        self.prompt_file = prompt_file
        self.contextual_prompt = self._load_prompt()
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-flash")
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
    
    def reload_prompt(self):
        """Reload prompt from file (useful after PromptEditor makes changes)"""
        self.contextual_prompt = self._load_prompt()

    def get_response(self, question: str):
        if self.model:
            combined_prompt = self.contextual_prompt + "\n\nSTUDENT'S QUESTION:\n" + question
            response = self.model.generate_content(combined_prompt)
            time.sleep(1) # Add a small delay
            return response.text
        else:
            return "Tutor bot not initialized due to API error."

# Expert Grader Model
class ExpertGrader:
    def __init__(self, answers_data: dict):
        self.answers = answers_data
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-flash")
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

    def grade_conversation(self, student_question: str, tutor_response: str):
        if not self.model or not self.chat:
            return "Expert grader not initialized due to API error."

        correct_answer = self.answers.get(student_question, "No expert answer available for this question.")

        grading_prompt = f"""You are an expert grader of educational tutoring conversations. Your task is to evaluate a tutor bot's performance based on specific pedagogical and interaction criteria. You will be provided with the student's question, the tutor's response, and the expert's 'correct' answer (if available).

**Grading Criteria:**

**Pedagogical Logic & Content Strategy:**
- Guides, Doesn't Solve: Uses sequential hints and Socratic questioning to lead the user to the solution, rather than providing the final answer outright.
- Adaptive Explanations: When a user indicates they're stuck, the bot offers the same concept explained in a different way (e.g., using an analogy, a code example, or a simpler definition).
- Accurate Error Analysis: Correctly identifies common misconceptions or errors in the user's input and provides targeted, constructive feedback.
- Scaffolds Complexity: Breaks down complex topics and problems into smaller, logical, and more manageable steps for the user to complete.
- Contextual Action: Tutor bot knows to give the direct answer when the question is for clarification and knows when to scaffold when the student is undertaking a problem solving exercise.
- Promotes Metacognition: Prompts the user to articulate their reasoning (e.g., "Can you explain why that line of code is necessary?").

**Interaction & Response Quality:**
- Context-Aware Responses: Demonstrates an ability to understand and remember the context of the current conversation, rather than treating each input as a brand new query.
- Effective Pacing: Delivers information in digestible chunks, avoiding overwhelming "walls of text" and waiting for user input before proceeding.
- Robust Input Parsing: Accurately interprets user intent, even with typos, slang, or ambiguously phrased questions.
- Clear Escape Hatches: Provides clear ways for a user to change the topic, ask for a menu, or restart if the conversation goes off-track.
- Consistent and Encouraging Tone: The bot's language is consistently programmed to be supportive, non-judgmental, and free of condescending or frustrating phrasing.

**Learning Pathway & Resource Integration:**
- Effective Onboarding & Goal Setting: Clearly frames the topic at the beginning of a session and helps the user define what they want to accomplish.
- Reinforces with Documentation: Provides timely and relevant links to specific sections of the official documentation to supplement explanations and encourage self-reliance.
- Fosters Transferable Skills: The overall goal of the interaction is to teach the user a process or framework for solving similar problems in the future.
- Offers Meaningful Summaries: Can effectively summarize key takeaways, new commands learned, or concepts covered at the end of a module or session.

**Conversation Details:**
Student Question: {student_question}
Tutor Bot Response: {tutor_response}
Expert's Correct Answer: {correct_answer}

**Your Evaluation:**
Based on the above criteria, please provide a concise grade (e.g., A, B, C, D, F) for the Tutor Bot's response, followed by a brief explanation for your grade, focusing on how well it adhered to the pedagogical logic and content strategy, interaction quality, and resource integration. If the expert answer is 'No expert answer available for this question.', focus your grading purely on the conversational and pedagogical aspects without comparing to an external correct answer.

Grade: 
Explanation: """

        response = self.chat.send_message(grading_prompt)
        time.sleep(1) # Add a small delay
        return response.text


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

def main():
    all_faq_questions, all_answers = load_answers_from_pkl()
    if not all_faq_questions:
        print("No questions loaded from answers.pkl.gz. Exiting.")
        return

    student = StudentImpersonator(all_faq_questions)
    tutor = TutorBot()
    # Pass all_answers to the grader
    grader = ExpertGrader(answers_data=all_answers)
    # Initialize LinkChecker
    link_checker = LinkChecker()

    # Simulate multi-turn conversation until student is satisfied
    conversation_history = []
    turn_count = 0
    current_student_question = None
    prev_tutor_response = None

    while True:
        turn_count += 1
        print(f"--- Turn {turn_count} ---")

        # Student asks question
        current_student_question = student.ask_question(last_tutor_response=prev_tutor_response)
        print(f"Student: {current_student_question}\n")

        if current_student_question == "I'm satisfied with my care":
            print("Conversation concluded by student satisfaction.\n")
            break

        # Tutor responds
        tutor_response = tutor.get_response(current_student_question)
        print(f"Tutor: {tutor_response}\n")

        # Check tutor response with LinkChecker
        link_check_results = link_checker.check_tutor_response(tutor_response)
        link_feedback = link_checker.generate_feedback_report(link_check_results)
        
        conversation_history.append({
            "student_question": current_student_question,
            "tutor_response": tutor_response,
            "link_check_results": link_check_results,
            "link_feedback": link_feedback
        })
        
        # Print link checker feedback
        print(f"Link Checker Feedback:\n{link_feedback}\n")
        
        prev_tutor_response = tutor_response # Update for the next student turn

    # Grade the conversation (using the last turn for now)
    if conversation_history:
        last_turn = conversation_history[-1]
        # If the last student question was the satisfaction message, use the previous turn for grading if available
        if last_turn["student_question"] == "I'm satisfied with my care" and len(conversation_history) > 1:
            last_turn = conversation_history[-2]

        grade = grader.grade_conversation(last_turn["student_question"], last_turn["tutor_response"])
        print(f"Grader's Evaluation for the last graded turn:\n{grade}\n")
    else:
        print("No conversation turns to grade.")

if __name__ == "__main__":
    main() 