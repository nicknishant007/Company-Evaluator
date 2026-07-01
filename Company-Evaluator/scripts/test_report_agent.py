import asyncio

from llms.factory import LLMFactory

from agents.report_agent import (
    ReportAgent,
)


async def main():

    llm = LLMFactory.get_llm()

    state = {


        "research":
        """
        Cera Sanitaryware Ltd. is one of India's leading manufacturers of sanitaryware,
        faucets, tiles, and wellness products. The company has built a premium brand
        through a strong dealer network and focuses on quality, innovation, and
        energy-efficient manufacturing. Its diversified product portfolio reduces
        dependence on a single business segment.
        """,

        "financial_analysis":
        """
        FY25 Revenue: ~₹1,891 Crore
        FY25 Net Profit: ~₹246 Crore
        Net Profit Margin: ~13%
        Debt-to-Equity Ratio: ~0.05x

        The company maintains a strong balance sheet with negligible debt and healthy
        profitability. Revenue growth has remained stable despite muted real-estate
        demand, supported by premium product sales and operational efficiency.
        """,

        "news_analysis":
        """
        Recent business updates indicate continued expansion in premium product lines,
        including the Senator luxury brand and affordable product initiatives.
        Management expects gradual demand recovery while focusing on margin protection
        and long-term market share growth.
        """,

        "risk_analysis":
        """
        Overall Risk Score: 3.5/10 (Low to Moderate)

        • Financial Risk: Low (almost debt-free)
        • Market Risk: Moderate (real-estate cycle dependency)
        • Competition Risk: Moderate
        • Commodity Cost Risk: Moderate

        The company's strong financial position reduces downside risk, although
        housing demand slowdown and raw material price fluctuations may impact
        short-term earnings.
        """,

        "valuation_analysis":
        """
        The stock trades at a premium valuation due to its strong brand, healthy
        return ratios, and debt-free status. Long-term fundamentals remain solid,
        but near-term upside depends on demand recovery in the housing sector.

        Recommendation: HOLD with Positive Long-Term Outlook.
        """


    }

    agent = ReportAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(
        result["final_report"]
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )