from llms.factory import LLMFactory

from agents.news_agent import (
    NewsAgent,
)

llm = LLMFactory.get_llm()


async def news_node(state):

    agent = NewsAgent(llm)

    news=await agent.run(state)

    return {

        "news_analysis": news

    }