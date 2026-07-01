from llms.factory import LLMFactory

from agents.finance_agent import (
    FinancialAnalysisAgent,
)

llm = LLMFactory.get_llm()


async def financial_node(state):

    print("ENter finance node")

    agent = FinancialAnalysisAgent(llm)

    print("calling agent")

    financial=await agent.run(state)
    print("Agent completed")

    return {

        "financial_analysis": financial

    }

