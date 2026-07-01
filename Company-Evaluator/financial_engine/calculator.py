from financial_engine.growth import GrowthCalculator
from financial_engine.profitability import ProfitabilityCalculator
from financial_engine.leverage import LeverageCalculator
from financial_engine.liquidity import LiquidityCalculator
from financial_engine.returns import ReturnCalculator
from financial_engine.cashflow import CashflowCalculator
from schemas.financial_metrics import FinancialMetrics

class FinancialCalculator:

    def calculate(
        self,
        financials,
    ):

        metrics = FinancialMetrics()

        # TODO:
        # Extract values from financials

        revenue = financials.total_revenue

        previous_revenue = financials.previous_revenue

        gross_profit = financials.gross_profit

        operating_income = financials.operating_income

        net_income = financials.net_income

        previous_net_income = financials.previous_net_income

        debt = financials.total_debt

        equity = financials.total_equity

        current_assets = financials.current_assets

        current_liabilities = financials.current_liabilities

        inventory = financials.inventory

        assets = financials.total_assets

        operating_cashflow = financials.operating_cash_flow

        capex = financials.capital_expenditure
        

        metrics.revenue_growth = (
            GrowthCalculator.revenue_growth(
                revenue,
                previous_revenue
            )
        )

        metrics.net_income_growth = (
            GrowthCalculator.net_income_growth(
                net_income,
                previous_net_income
            )
        )

        metrics.gross_margin = (
            ProfitabilityCalculator.gross_margin(
                gross_profit,
                revenue
            )
        )

        metrics.operating_margin = (
            ProfitabilityCalculator.operating_margin(
                operating_income,
                revenue
            )
        )

        metrics.net_margin = (
            ProfitabilityCalculator.net_margin(
                net_income,
                revenue
            )
        )

        metrics.debt_equity = (
            LeverageCalculator.debt_to_equity(
                debt,
                equity
            )
        )

        metrics.current_ratio = (
            LiquidityCalculator.current_ratio(
                current_assets,
                current_liabilities
            )
        )

        metrics.quick_ratio = (
            LiquidityCalculator.quick_ratio(
                current_assets,
                inventory,
                current_liabilities
            )
        )

        metrics.roe = (
            ReturnCalculator.roe(
                net_income,
                equity
            )
        )

        metrics.roa = (
            ReturnCalculator.roa(
                net_income,
                assets
            )
        )

        metrics.free_cash_flow = (
            CashflowCalculator.free_cash_flow(
                operating_cashflow,
                capex
            )
        )

        return metrics