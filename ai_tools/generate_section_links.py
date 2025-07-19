import os
import re

COURSE_DIR = '../course'  # relative to ai_tools/
COMBINED_MD = 'combined_documentation.md'
BASE_URL = 'https://introtoroboticsv2.readthedocs.io/en/latest/course/'

# Step 1: Collect all .rst files and their URLs
rst_links = []
for root, dirs, files in os.walk(COURSE_DIR):
    for file in files:
        if file.endswith('.rst'):
            rel_dir = os.path.relpath(root, COURSE_DIR)
            rel_path = os.path.join(rel_dir, file) if rel_dir != '.' else file
            url_path = rel_path.replace(os.sep, '/').replace('.rst', '.html')
            url = BASE_URL + url_path
            # Use the file stem as the key for matching
            section_key = os.path.splitext(file)[0].replace('_', ' ').title()
            rst_links.append({'section_key': section_key, 'url': url, 'file': file})

# Step 2: Read combined_documentation.md
with open(COMBINED_MD, encoding='utf-8') as f:
    lines = f.readlines()

# Step 3: For each .rst, find the first matching section header and insert the link after it
output_lines = []
used_sections = set()
for i, line in enumerate(lines):
    output_lines.append(line)
    m = re.match(r'^(#+)\s*(.+)', line)
    if m:
        header_title = m.group(2).strip().replace('_', ' ').title()
        for rst in rst_links:
            if rst['section_key'] == header_title and rst['section_key'] not in used_sections:
                # Insert the link after the header
                output_lines.append(f'[Read online documentation for this section]({rst["url"]})\n\n')
                used_sections.add(rst['section_key'])
                break

# Step 4: Write the updated file
with open(COMBINED_MD, 'w', encoding='utf-8') as f:
    f.writelines(output_lines) 