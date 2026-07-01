import asyncio

from llms.factory import LLMFactory

from agents.company_agent  import (
    CompanyResearchAgent,
)

from data_sources.factory import (
    DataSourceFactory
)


async def main():

    llm = LLMFactory.get_llm()

    yahoo = DataSourceFactory.yahoo()

    profile = await yahoo.get_company_profile(
        "AAPL"
    )
    
    state = {

        "profile": profile,
    }

    agent = CompanyResearchAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(
        result["research"]
    )


if __name__ == "__main__":

    asyncio.run(main())