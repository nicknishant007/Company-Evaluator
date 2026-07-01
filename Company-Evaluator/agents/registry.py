from agents.company_agent import (
    CompanyResearchAgent
)

from agents.finance_agent import (
    FinancialAnalysisAgent
)

from agents.news_agent import NewsAgent

from agents.risk_agent import RiskAgent

from agents.valuation_agent import ValuationAgent


class AgentRegistry:

    def __init__(self, llm):

        self.llm = llm

        self.agents = {

            "research": CompanyResearchAgent(
                llm
            ),

            "financial": FinancialAnalysisAgent(
                llm
            ),

            "news": NewsAgent(
                 llm
            ),

            "risk": RiskAgent(llm),

            "valuation": ValuationAgent(llm),
        }

    def get(
        self,
        name: str,
    ):

        return self.agents[name]