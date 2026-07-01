from agents.base import BaseAgent

from state.state import CompanyState
class ValuationAgent(
    BaseAgent
):

    prompt_file = "valuation_analysis.txt"

    def build_prompt(
        self,
        state:CompanyState,
    ):

        return f"""
{self.prompt}

Company Research:

{state["research"]}


Financial Analysis:

{state["financial_analysis"]}


News Analysis:

{state["news_analysis"]}


Risk Analysis:

{state["risk_analysis"]}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["valuation_analysis"] = response