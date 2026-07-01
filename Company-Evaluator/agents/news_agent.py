from agents.base import BaseAgent

from state.state import CompanyState

class NewsAgent(
    BaseAgent
):

    prompt_file = "newsandweb.txt"

    def build_prompt(
        self,
        state:CompanyState,
    )->str:

        return f"""
{self.prompt}

News Articles:

{state["news"]}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["news_analysis"] = response