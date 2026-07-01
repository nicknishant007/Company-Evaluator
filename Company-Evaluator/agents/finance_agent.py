
from agents.base import BaseAgent

from state.state import CompanyState


class FinancialAnalysisAgent(
    BaseAgent
):
    prompt_file="financial_analysis.txt"
    def build_prompt(
        self,
        state:CompanyState,
    )->str:
        print(type(state["financials"]))
        print(type(state["financial_metrics"]))
        print(type(state["stock"]))


        return f"""
{self.prompt}

Financial Data:

{state["financials"].model_dump_json(indent=2)}

Calculated Ratios:

{state["financial_metrics"].model_dump_json(indent=2)}

Stock Data:

{state["stock"].model_dump_json(indent=2)}
"""

    def update_state(
        self,
        state:CompanyState,
        response,
    ):

        state["financial_analysis"] = response