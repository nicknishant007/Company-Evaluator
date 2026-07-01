class ReturnCalculator:

    @staticmethod
    def roe(
        net_income,
        equity,
    ):

        if net_income is None or equity is None or equity == 0:
            return None

        return (
            net_income
            / equity
        ) * 100

    @staticmethod
    def roa(
        net_income,
        assets,
    ):

        if net_income is None or assets is None or assets == 0:
            return None

        return (
            net_income
            / assets
        ) * 100