class GrowthCalculator:

    @staticmethod
    def revenue_growth(
        current: float,
        previous: float,
    ):

        if current is None or previous is None or previous == 0:
            return None

        return (
            (current - previous)
            / previous
        ) * 100

    @staticmethod
    def net_income_growth(
        current: float,
        previous: float,
    ):
        if current is None or previous is None or previous == 0:
            return None

        return (
            (current - previous)
            / previous
        ) * 100