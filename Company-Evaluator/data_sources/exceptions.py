class DataSourceError(Exception):
    pass


class AuthenticationError(
    DataSourceError
):
    pass


class RateLimitError(
    DataSourceError
):
    pass


class ProviderUnavailableError(
    DataSourceError
):
    pass


class InvalidTickerError(
    DataSourceError
):
    pass