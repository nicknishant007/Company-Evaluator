from agents.base import BaseAgent

from state.state import CompanyState 

class ReportAgent(
    BaseAgent
):

    prompt_file = "report_gen.txt"

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


Valuation Analysis:

{state["valuation_analysis"]}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["report"] = response