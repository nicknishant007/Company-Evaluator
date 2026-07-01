from llms.factory import LLMFactory

from agents.valuation_agent import ValuationAgent

llm = LLMFactory.get_llm()


async def valuation_node(state):

    agent = ValuationAgent(llm)

    valuation = await agent.run(state)

    return {

        "valuation_analysis": valuation

    }