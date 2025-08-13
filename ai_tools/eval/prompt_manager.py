import os
from pathlib import Path
from typing import Optional

class PromptManager:
    """Manages loading and saving prompt files"""
    
    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = Path(prompts_dir)
        self.prompts_dir.mkdir(exist_ok=True)
    
    def load_prompt(self, prompt_name: str) -> str:
        """Load a prompt from file"""
        prompt_path = self.prompts_dir / prompt_name
        
        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            raise RuntimeError(f"Error reading prompt file {prompt_path}: {e}")
    
    def save_prompt(self, prompt_name: str, content: str) -> bool:
        """Save a prompt to file"""
        prompt_path = self.prompts_dir / prompt_name
        
        try:
            with open(prompt_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error saving prompt file {prompt_path}: {e}")
            return False
    
    def prompt_exists(self, prompt_name: str) -> bool:
        """Check if a prompt file exists"""
        prompt_path = self.prompts_dir / prompt_name
        return prompt_path.exists()
    
    def list_prompts(self) -> list[str]:
        """List all available prompt files"""
        return [f.name for f in self.prompts_dir.glob("*.txt")]
    
    def get_prompt_path(self, prompt_name: str) -> Path:
        """Get the full path to a prompt file"""
        return self.prompts_dir / prompt_name
