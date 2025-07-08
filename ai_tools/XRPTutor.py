"""
XRPTutor - Expert Tutoring System for XRP Robotics

This module provides comprehensive, accurate responses to XRP robotics questions
with complete code solutions and documentation references.
"""

import os
from typing import Optional

class XRPTutor:
    """
    XRPCode Buddy - A friendly and expert programming tutor specializing in XRP robotics education.
    
    Core Philosophy:
    - Provide accurate, detailed responses with complete code solutions
    - Reference comprehensive XRP documentation with embedded links
    - Explain concepts using clear, intuitive language and real-world analogies
    - Focus on practical implementation and immediate usability
    - Ensure technical accuracy and provide working code examples
    """
    
    def __init__(self, documentation_path: str = "combined_documentation.md"):
        """
        Initialize the XRP Tutor with documentation context.
        
        Args:
            documentation_path: Path to the combined XRP documentation markdown file
        """
        self.documentation = self._load_documentation(documentation_path)
        self.core_prompt = self._build_core_prompt()
        
    def _load_documentation(self, doc_path: str) -> str:
        """Load the XRP documentation as context."""
        try:
            with open(doc_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Warning: Documentation file '{doc_path}' not found.")
            return "Documentation not available."
    
    def _build_core_prompt(self) -> str:
        """Build the core expert tutoring system prompt."""
        return """**XRP ROBOTICS EXPERT SYSTEM**

You are XRPCode Buddy, a friendly and expert programming tutor specializing in XRP robotics education. Your primary mission is to provide accurate, detailed, and comprehensive responses to XRP robotics questions with complete code solutions, explanations, and documentation references.

**CORE RESPONSE PHILOSOPHY:**
• Provide precise, detailed answers that directly solve the user's problem
• Include complete, working code solutions when requested
• Reference specific XRP documentation sections with embedded links
• Explain the "why" behind solutions using clear, intuitive language
• Use real-world analogies to make concepts more understandable
• Provide comprehensive examples and code snippets
• Focus on practical implementation and immediate usability
• Ensure all responses are technically accurate and tested

**DOCUMENTATION INTEGRATION & CODE SNIPPETS:**
Actively use the XRP documentation to provide authoritative answers:

• **Comprehensive Documentation References**: Always cite specific API functions, sensor guides, and curriculum sections
• **Embed Documentation Links**: Include clickable links from the documentation so users can explore further
• **Complete Code Examples**: Provide full, working code solutions with detailed explanations
• **Function Signatures**: Show exactly what parameters functions expect and return
• **Sensor Implementation Examples**: Demonstrate complete sensor usage patterns with proper setup
• **API Usage Patterns**: Show best practices for using XRP library functions
• **Real Code from Documentation**: Extract and adapt actual code examples from the XRP curriculum
• **Link to Sources**: Always include URLs when citing specific documentation sections

**RESPONSE STRUCTURE:**
For each response, provide:

• **Direct Answer**: Immediately address the specific question or problem
• **Complete Code Solution**: Full working code when applicable, properly formatted
• **Detailed Explanation**: Step-by-step breakdown of how and why the solution works
• **Documentation References**: Specific sections and links to relevant XRP documentation
• **Real-World Context**: Analogies and practical applications to enhance understanding
• **Additional Resources**: Related topics and further learning opportunities
• **Implementation Notes**: Any important considerations, limitations, or best practices

**TECHNICAL ACCURACY REQUIREMENTS:**
• All code must be syntactically correct and follow XRP library conventions
• Reference only functions and methods that actually exist in the XRP documentation
• Provide accurate parameter names, types, and usage patterns
• Include proper import statements and setup code
• Ensure all examples are complete and runnable
• Test conceptual explanations against documented behavior
• Cite specific documentation sections for verification

**COMMUNICATION STYLE:**
• Friendly and approachable while maintaining technical expertise
• Use clear, everyday language alongside technical terms
• Provide intuitive explanations with practical analogies
• Be comprehensive yet concise in explanations
• Focus on immediate usability and practical application
• Maintain enthusiasm for robotics and programming concepts
"""

    def generate_response_prompt(self, question: str) -> str:
        """
        Generate a complete prompt for responding to a user question.
        
        Args:
            question: The user's question about XRP robotics
            
        Returns:
            Complete prompt ready for the AI tutoring system
        """
        prompt = self.core_prompt + "\n\n"
        
        # Add documentation context
        prompt += "**XRP ROBOTICS DOCUMENTATION:**\n"
        prompt += "Complete XRP robotics documentation is available including API references, tutorials, and programming guides. Use this as your authoritative source for XRP concepts, functions, and best practices. The documentation includes embedded links for sections and subsections - always include these clickable URLs when referencing specific curriculum content so users can explore further.\n\n"
        
        # Add the question
        prompt += "**USER'S QUESTION:**\n"
        prompt += question + "\n\n"
        
        # Add response guidelines
        prompt += "**YOUR RESPONSE GUIDELINES:**\n"
        prompt += "Provide a comprehensive, accurate response that:\n\n"
        prompt += "1. **Directly answers** the specific question or problem\n"
        prompt += "2. **Includes complete code** solutions when applicable\n"
        prompt += "3. **Explains the solution** step-by-step with clear reasoning\n"
        prompt += "4. **References documentation** with specific sections and links\n"
        prompt += "5. **Uses analogies** and real-world context for better understanding\n"
        prompt += "6. **Provides additional resources** for further learning\n"
        prompt += "7. **Ensures technical accuracy** with proper syntax and function usage\n\n"
        prompt += "**Remember**: Be thorough, accurate, and immediately helpful while maintaining a friendly, enthusiastic tone about XRP robotics programming."
        
        return prompt
    
    def get_documentation_section(self, topic: str) -> str:
        """
        Extract relevant documentation section for a given topic.
        
        Args:
            topic: Topic to search for in documentation
            
        Returns:
            Relevant documentation section
        """
        if not self.documentation:
            return "Documentation not available."
        
        # Simple search for topic in documentation
        lines = self.documentation.split('\n')
        relevant_lines = []
        in_relevant_section = False
        
        for line in lines:
            if topic.lower() in line.lower():
                in_relevant_section = True
                relevant_lines.append(line)
            elif in_relevant_section and line.startswith('#'):
                # End of section
                break
            elif in_relevant_section:
                relevant_lines.append(line)
        
        return '\n'.join(relevant_lines[:50])  # Limit to 50 lines

    def format_code_snippet(self, code: str, explanation: str = "") -> str:
        """
        Format a code snippet for educational purposes.
        
        Args:
            code: Code snippet to format
            explanation: Optional explanation of the code
            
        Returns:
            Formatted code snippet with explanation
        """
        formatted = f"```python\n{code}\n```"
        if explanation:
            formatted += f"\n\n{explanation}"
        return formatted
    
    def get_documentation_content(self) -> str:
        """Get the full documentation content."""
        return self.documentation 