import asyncio

from llms.factory import LLMFactory

from agents.finance_agent import FinancialAnalysisAgent

from data_sources.factory import DataSourceFactory


async def main():
    llm= LLMFactory.get_llm()

    yahoo=DataSourceFactory.yahoo()

    financials= await yahoo.get_financials(
        "AAPL"
    )
    state = {

        "financials": financials,

        "stock": stock,
    }

    agent = FinancialAnalysisAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(
        result["financial_analysis"]
    )


if __name__ == "__main__":

    asyncio.run(main())