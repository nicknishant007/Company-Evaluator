from llms.factory import LLMFactory

from agents.risk_agent import RiskAgent

llm = LLMFactory.get_llm()


async def risk_node(state):
    print(state.keys())
    agent = RiskAgent(llm)

    risk=await agent.run(state)

    return {

        "risk_analysis": risk

    }