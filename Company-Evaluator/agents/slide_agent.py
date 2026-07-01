from state.state import CompanyState

from agents.base import BaseAgent

class SlideAgent(BaseAgent):

    prompt_file="slides.txt"

    def build_prompt(self,
                     state:CompanyState
                     )->str:
                        
                        return f"""
    {self.prompt}

    Report:{state["report"]}"""
        