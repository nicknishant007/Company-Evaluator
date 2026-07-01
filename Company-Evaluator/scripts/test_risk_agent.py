import asyncio

from llms.factory import LLMFactory

from agents.risk_agent import (
    RiskAgent,
)


async def main():

    llm = LLMFactory.get_llm()

    state = {

        "research":

        """
Apple is the largest consumer electronics company
with a strong ecosystem.
""",

        "financial_analysis":

        """
Revenue growing.
Margins healthy.
Debt low.
Cash flow positive.
""",

        "news_analysis":

        """
Apple launches AI products.
EU antitrust investigation continues.
Overall sentiment Neutral.
"""
    }

    agent = RiskAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(

        result["risk_analysis"]

    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )