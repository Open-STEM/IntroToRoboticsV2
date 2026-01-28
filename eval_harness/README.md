# Eval Harness

This directory contains the refactored evaluation harness for assessing and improving LLM-based tutors for XRP robotics.

## Purpose

The Eval Harness provides a structured pipeline to:
1.  **Generate realistic user FAQ questions** based on course documentation and a user persona.
2.  **Simulate tutor-user interactions** for these questions.
3.  **Evaluate tutor performance** using an expert and a grader LLM.
4.  **Test tutor robustness** against jailbreak attempts.
5.  **Provide actionable feedback** and **suggest improvements** to the tutor's prompt.

## Setup

To get this evaluation harness running, follow these steps:

1.  **Navigate to the project root:**
    Make sure your current directory in the terminal is `IntroToRoboticsV2`.

2.  **Conda Environment (Recommended):**
    A `conda` environment is recommended to manage dependencies. While `environment.yml` was discussed, for simplicity and to keep the environment setup within the current repository's `requirements.txt` context, please ensure your environment has the necessary packages installed.

    First, ensure you have a Python environment (e.g., `conda` or `venv`) activated. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` has been updated to include `google-generativeai`, `pydantic`, and `python-dotenv`.)*

3.  **Google AI API Key:**
    The harness interacts with Google's Gemini LLMs. You need an API key for this.
    1.  Obtain your `GOOGLE_AI_API_KEY` from the Google AI Studio.
    2.  Copy the `env_example` file to `.env` within this `eval_harness/` directory:
        ```bash
        cp eval_harness/env_example eval_harness/.env
        ```
    3.  Open the newly created `.env` file and replace `'your_google_ai_api_key_here'` with your actual API key:
        ```
        GOOGLE_AI_API_KEY='your_api_ai_key_here'
        ```
        **Important:** Do not commit your `.env` file to version control if it contains your actual key.

## Usage

You can run the evaluation pipeline from the project root directory. The main script (`eval_harness.main`) offers two modes: **FAQ Generation & Evaluation** (default) and **Jailbreak Testing**.

### Default Mode: FAQ Generation & Evaluation

This mode generates diverse questions and evaluates the tutor's teaching performance.

```bash
python3 -m eval_harness.main
```

### Jailbreak Testing Mode

This mode generates questions specifically designed to bypass the tutor's guardrails and attempts to extract full code solutions. It's used to test the robustness of the tutor's prompt.

```bash
python3 -m eval_harness.main --jailbreak
```
You can also specify the number of jailbreak attempts:
```bash
python3 -m eval_harness.main --jailbreak --num_jailbreak_attempts 5
```

### What it does when you run it:

1.  **In Default Mode (FAQ Generation & Evaluation):**
    *   **Generates FAQ Questions:** Creates a set of realistic user-like FAQ questions about XRP robotics using an LLM, based on the `combined_documentation.md` and `faq_user_persona_prompt.txt`. These are saved to `eval_harness/generated_faqs.txt`.
    *   **Evaluates Tutor Performance:** Samples a few questions and simulates conversations where an Expert provides a benchmark, your Tutor (guided by `tutor_prompt.txt`) responds, and a Student LLM interacts. A Grader assesses the Tutor's performance and prompt adherence.
    *   Evaluation results are recorded in `eval_harness/feedback_history.json`.

2.  **In Jailbreak Testing Mode:**
    *   **Generates Jailbreak Attempts:** Uses a specialized "Jailbreak Agent" (guided by `jailbreak_prompt.txt`) to create prompts designed to circumvent the tutor's guardrails.
    *   **Tests Tutor Robustness:** These jailbreak attempts are then fed to the Tutor LLM. The evaluation process assesses how well the Tutor resists providing full code solutions or breaking its persona.

3.  **Provides a Summary:**
    *   An overall summary of the evaluations, including average scores and recurring issues, will be printed to your console.

4.  **Optional Tutor Prompt Improvement:**
    *   You'll be prompted to apply suggested improvements to your `tutor_prompt.txt`. If you agree, an "Editor" LLM will automatically revise the prompt based on the feedback.
    *   You'll also have an option to clear the `feedback_history.json`.

---

### Files in this folder:

*   `env_example`: An example file for your API key configuration. Copy this to `.env` and fill in your key.
*   `README.md`: This file.
*   `combined_documentation.md`: The curriculum documentation used by the LLMs.
*   `faq_generator.py`: Module responsible for generating FAQ questions.
*   `evaluator.py`: Module containing the core logic for simulating and evaluating conversations.
*   `jailbreak_agent.py`: Module responsible for generating jailbreak attempts.
*   `main.py`: The main entry point for running the entire evaluation pipeline.
*   `prompts/`: Directory containing various role-based prompts:
    *   `expert_prompt.txt`
    *   `tutor_prompt.txt`
    *   `student_prompt.txt` (for the student role in evaluation)
    *   `faq_user_persona_prompt.txt` (for FAQ generation)
    *   `jailbreak_prompt.txt`
*   `feedback_history.json`: Stores past evaluation results.
*   `generated_faqs.txt`: Stores the dynamically generated FAQ questions (in default mode).