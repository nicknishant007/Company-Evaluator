import asyncio

from llms.factory import LLMFactory

from agents.valuation_agent import (
    ValuationAgent,
)


async def main():

    llm = LLMFactory.get_llm()

    state = {

        "research":
        """
        Titan Company Ltd. is one of India's leading lifestyle companies with a diversified portfolio across
        Jewellery (Tanishq, Mia, Zoya), Watches, Wearables, Eyewear, and Emerging Businesses.
        The company benefits from a trusted brand image, a strong omnichannel retail network of 3,000+
        stores, and consistent expansion in premium consumer segments.
        """,

        "financial_analysis":
        """
        FY25 Revenue: ₹57,819 Cr (+22% YoY)
        Net Profit: ₹4,535 Cr (+5% YoY)
        EBIT Margin: ~10.8%
        ROE: ~31%
        Titan maintains healthy revenue growth driven by strong jewellery demand, although margins remain
        under pressure due to gold price volatility and expansion investments.
        Overall financial health remains strong with consistent cash generation and low debt.
        """,

        "news_analysis":
        """
        Titan continues to expand its jewellery and wearable businesses across India while increasing
        its premium product offerings. Strong festive demand and store expansion have supported sales
        growth. However, fluctuations in gold prices and changing consumer spending patterns remain
        key factors influencing short-term performance.
        """,

        "risk_analysis":
        """
        Overall Risk Score: 3.2/10 (Low Risk)

        Business Risk: Low
        Financial Risk: Low
        Market Risk: Moderate (gold price volatility)
        Regulatory Risk: Low
        Competition Risk: Moderate

        Titan's diversified business model, strong brand value, and market leadership reduce long-term
        risk, although dependence on jewellery sales and precious metal prices introduces moderate
        cyclical risk.
        """


    }

    agent = ValuationAgent(
        llm
    )

    result = await agent.run(
        state
    )

    print(
        result["valuation_analysis"]
    )


if __name__ == "__main__":

    asyncio.run(main())