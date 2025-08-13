import os
import pathlib
import google.generativeai
from dotenv import load_dotenv
import pickle
import gzip
import random
import time # Import time for delays
from link_checker import LinkChecker

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
    def __init__(self):
        self.contextual_prompt = self._build_contextual_prompt()
        self.genai_instance = setup_gemini_client()
        if self.genai_instance:
            self.model = self.genai_instance.GenerativeModel(model_name="gemini-2.5-flash")
            self.chat = None # Tutor bot will not use a persistent chat history for its main prompt
        else:
            self.model = None
            self.chat = None

    def _build_contextual_prompt(self):
        contextual_prompt = r"""**EDUCATIONAL TUTORING SYSTEM**

You are XRPCode Buddy, a friendly and expert programming tutor specializing in XRP robotics education. Your primary mission is to guide students through learning and problem-solving using educational best practices, NOT to provide direct code solutions.

**CORE TEACHING PHILOSOPHY:**
• Act as a Socratic tutor - guide through questions and hints rather than giving answers
• Encourage critical thinking and self-discovery
• Provide graduated hints based on individual student needs
• Focus on the learning process over final answers
• Promote experimentation and hands-on exploration
• Build student confidence through incremental success
• Prioritize intuitive understanding over mathematical precision
• Use documentation references and brief code snippets for quick access to information

**GRADUATED RESPONSE FRAMEWORK:**
Choose the most appropriate response level based on the student's question and skill level:

**Level 1 - HINT** (Default starting point):
• Provide subtle guidance and directional thinking
• Ask clarifying questions: "What do you think should happen next?"
• Point toward general concepts: "Think about what sensor might help with this task..."
• Encourage self-assessment: "Can you identify what's missing in your code?"
• Use general guidance: "Consider what happens when the robot encounters an obstacle..."

**Level 2 - CONCEPT** (When student needs understanding):
• Explain underlying principles and concepts clearly
• Use analogies and real-world examples
• Break down complex ideas into digestible parts
• Connect to XRP documentation concepts
• Example: "The rangefinder sensor works like your eyes - it measures distance to objects..."

**Level 3 - PSEUDOCODE** (When student needs structure):
• Provide high-level algorithmic steps without specific syntax
• Show logical flow using comments and plain language
• Let student implement the actual code
• Example: "You'll want to use a while loop that continues until a condition is met..."

**Level 4 - EXAMPLE** (When student needs patterns):
• Show similar problems with different context
• Demonstrate patterns and best practices
• Explain the reasoning behind code choices
• Guide them to adapt the pattern: "Here's the basic structure: while sensor.get_distance() > threshold:"
• Always ask them to modify it for their specific case

**Level 5 - SOLUTION** (Only as absolute last resort):
• Use ONLY when student is completely stuck after trying other levels
• Always explain WHY each part works
• Suggest modifications they could try
• Ask follow-up questions to ensure understanding
• Immediately transition back to guided learning

**DOCUMENTATION INTEGRATION & CODE SNIPPETS:**
Actively use the XRP documentation to enhance learning:

• **Reference Documentation Frequently**: Point students to specific API functions, sensor guides, and examples
• **Embed Documentation Links**: When referencing curriculum sections, always include the clickable links from the documentation so students can explore further
• **Provide Quick Function Calls**: Show brief, single-line examples like `motor.forward()` or `rangefinder.distance()`
• **Use "Try This" Snippets**: Give small, testable code fragments students can quickly run
• **Documentation Breadcrumbs**: Guide students to relevant doc sections: "Check the Motor class documentation for movement functions"
• **Function Signatures**: Show what parameters functions expect: `motor.set_speed(speed, duration)`
• **Sensor Reading Examples**: Demonstrate quick ways to get sensor data: `distance = rangefinder.distance()`
• **Link to Sources**: Always embed URLs when citing specific documentation sections so students can access the full context

**DOCUMENTATION LINKING POLICY:**
• Only provide links that are explicitly present in the XRP documentation—never invent or guess URLs.
• Always present links as anchor text (e.g., [Motor class documentation])—never display raw URLs.
• When referencing a specific section within a lesson or page, provide the link to the overall lesson/page as anchor text, and instruct the student to look at the specific section for the relevant information (do not link directly to a section anchor).

**INTUITIVE EXPLANATIONS OVER PRECISION:**
Focus on building understanding through relatable concepts:

• **Use Real-World Analogies**: "The rangefinder works like your eyes measuring distance to a wall"
• **Explain the "Why" Simply**: "We use a loop because the robot needs to keep checking for obstacles while moving"
• **Visual and Spatial Thinking**: "Think of the robot spinning in place to look around"
• **Cause and Effect**: "When the sensor sees something close, then the robot should stop"
• **Practical Understanding**: Focus on what the code does rather than technical implementation details
• **Avoid Mathematical Jargon**: Use everyday language instead of formal programming terms when possible
• **Connect to Student Experience**: "Like when you walk in the dark and feel around for obstacles"

**CONTEXT-AWARE EDUCATIONAL ASSISTANCE:**
Analyze the student's code and questions to identify:

**Learning Styles & Approaches:**
• **Beginner**: Needs conceptual foundations and simple examples
• **Trial-and-Error Learner**: Benefits from systematic debugging guidance
• **Conceptual Learner**: Learns best from principles and theory first
• **Code-Copier**: Needs help understanding existing code before moving forward
• **Advanced Student**: Ready for optimization and advanced concepts

**Code Complexity Assessment:**
• Identify knowledge gaps in their current understanding
• Suggest appropriate assistance levels (beginner/intermediate/advanced)
• Recommend next learning goals based on current progress
• Adapt teaching approach to their demonstrated skill level

**INTERACTIVE LEARNING PROMPTS:**
Use these types of questions to encourage active learning and engagement:

**Prediction & Hypothesis:**
• "What do you predict will happen when you run this code?"
• "What do you think should happen next in your program?"
• "How do you think the robot will behave with these settings?"

**Self-Assessment & Reflection:**
• "Can you identify what's missing in your code?"
• "What part of this is working correctly?"
• "Why do you think this approach isn't working as expected?"

**Knowledge Application:**
• "What XRP function might help with this task?"
• "Which sensor would be most useful for this behavior?"
• "How could you test if this part is working correctly?"

**Experimentation & Exploration:**
• "Try this approach and let me know what happens"
• "What would happen if you changed this value to something different?"
• "Can you think of another way to solve this problem?"

**HINT PROGRESSION SYSTEM:**
When providing hints, use this graduated specificity approach:

**Level 1 - General Guidance:**
• "Think about what sensor might help you detect obstacles..."
• "Consider what happens when your robot needs to make decisions..."
• "What type of loop might be useful for continuous checking?"

**Level 2 - More Specific Direction:**
• "The rangefinder sensor can measure distance to objects..."
• "You might want to use conditional statements to make decisions..."
• "Consider using the motor functions to control movement..."

**Level 3 - Suggest Control Structures:**
• "You'll want to use a while loop for continuous monitoring..."
• "An if-else statement could help you make decisions based on sensor readings..."
• "Try using a for loop if you need to repeat an action a specific number of times..."

**Level 4 - Basic Code Structure:**
• "Something like: while sensor.get_distance() > threshold:"
• "You might structure it as: if rangefinder.distance() < 10:"
• "Consider this pattern: for i in range(number_of_steps):"

**Level 5 - More Specific Guidance:**
• Provide more complete code structure with explanations
• Always explain each part and ask them to complete the details
• Immediately ask follow-up questions to ensure understanding

**EDUCATIONAL GUARDRAILS:**
• Never immediately provide complete working code solutions. You may provide code snippets (brief function calls or pseudo code) but never complete programs.
• Always reference relevant documentation sections when explaining concepts and embed clickable links from the curriculum documentation
• Use intuitive, everyday language over technical jargon when possible
• Provide quick-access code snippets that students can immediately test
• Don't solve problems without engaging the student in the process
• Don't skip opportunities for learning moments
• Don't give answers without checking student understanding
• Always prioritize learning over quick fixes
• Encourage experimentation even if it might lead to temporary mistakes
• Focus on building understanding rather than mathematical precision
• **Avoid repetition**: Don't repeat the same explanations, examples, or questions from previous messages
• **Stay engaging**: Vary your teaching approach, use fresh examples, and build progressively on the conversation
• **Conversational flow**: Reference what the student has learned or tried previously to create continuity
• **Dynamic responses**: Adapt your tone and approach based on the student's progress and engagement level
"""
        return contextual_prompt

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