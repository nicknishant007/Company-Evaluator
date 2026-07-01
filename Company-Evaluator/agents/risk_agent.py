from agents.base import BaseAgent

from state.state import CompanyState
class RiskAgent(
    BaseAgent
):

    prompt_file = "risk_analysis.txt"

    def build_prompt(
        self,
        state:CompanyState,
    )->str:

        return f"""
{self.prompt}

Company Research:

{state["research"]}


Financial Analysis:

{state["financial_analysis"]}


News Analysis:

{state["news_analysis"]}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["risk_analysis"] = response