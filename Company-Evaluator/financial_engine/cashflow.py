class CashflowCalculator:

    @staticmethod
    def free_cash_flow(
        operating_cashflow,
        capex,
    ):
        if operating_cashflow is None or capex is None:
            return None

        return (
            operating_cashflow
            - capex
        )