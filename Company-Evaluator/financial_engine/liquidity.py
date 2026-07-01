class LiquidityCalculator:

    @staticmethod
    def current_ratio(
        current_assets,
        current_liabilities,
    ):

        if current_assets is None or current_liabilities is None or current_liabilities == 0:
            return None

        return (
            current_assets
            / current_liabilities
        )

    @staticmethod
    def quick_ratio(
        current_assets,
        inventory,
        current_liabilities,
    ):

        if (current_liabilities == 0 or inventory is None):
            return None

        return (
            current_assets
            - inventory
        ) / current_liabilities