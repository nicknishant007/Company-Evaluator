from llms.factory import LLMFactory

from agents.slide_agent import SlideAgent

llm = LLMFactory.get_llm()


async def slide_node(state):

    agent = SlideAgent(llm)

    slides = await agent.run(state)

    return {

        "slides_content": slides

    }