import os
import re

def identify_lesson_files():
    """
    Identifies reStructuredText (.rst) lesson files within the specified course directory
    by checking for a top-level title (underlined with '===').
    
    Args:
        (None: course_dir is now determined dynamically)
        
    Returns:
        list: A list of absolute paths to the identified lesson files.
    """
    # Determine the project root based on the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level from ai_tools to IntroToRoboticsV2
    project_root = os.path.dirname(script_dir)
    course_dir = os.path.join(project_root, "course")

    lesson_files = []
    title_pattern = re.compile(r"^={3,}$") # Matches a line with at least 3 equals signs
    
    abs_course_dir = os.path.abspath(course_dir)
    print(f"[DEBUG] Starting identify_lesson_files in course_dir: {course_dir}")
    print(f"[DEBUG] Absolute course_dir path: {abs_course_dir}")
    if not os.path.exists(abs_course_dir):
        print(f"[DEBUG] Error: course_dir does not exist at {abs_course_dir}")
        return []

    for root, _, files in os.walk(abs_course_dir):
        print(f"[DEBUG] Walking directory: {root}")
        for file in files:
            filepath = os.path.join(root, file)
            print(f"[DEBUG] Processing file: {filepath}")
            if not file.endswith(".rst"):
                print(f"[DEBUG] Skipping {file}: Not an .rst file")
                continue
            if file == "index.rst":
                print(f"[DEBUG] Skipping {file}: Is an index.rst file")
                continue
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    first_few_lines = [next(f) for _ in range(5)] # Read first few lines to check for title
                    print(f"[DEBUG] First 5 lines of {file}:\n{''.join(first_few_lines).strip()}")
                    # Check for a line that matches the title pattern (e.g., ===)
                    # and ensure it's preceded by some text (the title itself)
                    found_title = False
                    for i, line in enumerate(first_few_lines):
                        if title_pattern.match(line.strip()):
                            if i > 0 and first_few_lines[i-1].strip(): # Check if there's a title above it
                                lesson_files.append(filepath)
                                print(f"[DEBUG] Identified lesson file: {filepath}")
                                found_title = True
                                break # Found a lesson file, move to next file
                    if not found_title:
                        print(f"[DEBUG] {file} did not match title pattern.")
            except Exception as e:
                print(f"[DEBUG] Error reading file {filepath}: {e}")
    print(f"[DEBUG] Finished identify_lesson_files. Found {len(lesson_files)} lesson files.")
    return lesson_files

if __name__ == "__main__":
    # Example usage
    lesson_paths = identify_lesson_files()
    print("Identified Lesson Files (with '===' title):")
    for path in lesson_paths:
        print(path) 