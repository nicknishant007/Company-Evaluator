from financial_engine.calculator import (
    FinancialCalculator
)


async def financial_calculator_node(
    state
):
    print(f"Enter financial cal")
    calculator = FinancialCalculator()

    metrics = calculator.calculate(

        state["financials"]

    )
    print(f"these are the metric{metrics}")

    return {

        "financial_metrics": metrics

    }