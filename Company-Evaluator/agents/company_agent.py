
from agents.base import BaseAgent

from state.state import CompanyState


class CompanyResearchAgent(
    BaseAgent
):
    prompt_file="company_research.txt"

    def build_prompt(
        self,
        state:CompanyState,
    )->str:

        profile = state["profile"]

        return f"""
{self.prompt}

Comapny Information:
{profile.model_dump_json(indent=2)}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["research"] = response