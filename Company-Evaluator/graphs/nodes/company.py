from llms.factory import LLMFactory
from agents.company_agent import CompanyResearchAgent

llm = LLMFactory.get_llm()


async def company_node(state):

    agent = CompanyResearchAgent(llm)

    research=await agent.run(state)

    return {

        "research": research

    }