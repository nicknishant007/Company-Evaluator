class ProfitabilityCalculator:

    @staticmethod
    def gross_margin(
        gross_profit,
        revenue,
    ):

        if(
            gross_profit is None
            or revenue is None
            or revenue==0
        ):
            return None

        return (
            gross_profit
            / revenue
        ) * 100

    @staticmethod
    def operating_margin(
        operating_income,
        revenue,
    ):

        if(
            operating_income is None
            or revenue is None
            or revenue==0
        ):
            return None

        return (
            operating_income
            / revenue
        ) * 100

    @staticmethod
    def net_margin(
        net_income,
        revenue,
    ):

        if (
        net_income is None
        or revenue is None
        or revenue == 0
    ):
            return None

        return (
            net_income
            / revenue
        ) * 100