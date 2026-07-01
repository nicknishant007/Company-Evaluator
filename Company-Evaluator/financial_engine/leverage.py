class LeverageCalculator:

    @staticmethod
    def debt_to_equity(
        debt,
        equity,
    ):

        if debt is None or equity is None or equity == 0:
            return None

        return debt / equity

    @staticmethod
    def interest_coverage(
        ebit,
        interest,
    ):

        if ebit is None or interest is None or interest == 0:
            return None 

        return ebit / interest