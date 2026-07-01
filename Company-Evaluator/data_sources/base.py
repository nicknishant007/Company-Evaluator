from abc import ABC
from abc import abstractmethod


class BaseDataSource(ABC):

    @abstractmethod
    async def get_company_profile(
        self,
        ticker: str,
    ):
        pass

    @abstractmethod
    async def get_financials(
        self,
        ticker: str,
    ):
        pass

    @abstractmethod
    async def get_stock_data(
        self,
        ticker: str,
    ):
        pass