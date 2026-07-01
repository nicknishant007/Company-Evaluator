import asyncio

from llms.factory import LLMFactory

from agents.news_agent import (
    NewsAgent,
)


async def main():

    llm = LLMFactory.get_llm()

    state = {

        "news": [

            {
                "title":
                "Apple launches new AI features",

                "summary":
                "Apple announced major AI upgrades."
            },

            {
                "title":
                "EU investigates Apple App Store",

                "summary":
                "Regulators continue antitrust review."
            },
        ]
    }

    agent = NewsAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(
        result[
            "news_analysis"
        ]
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )