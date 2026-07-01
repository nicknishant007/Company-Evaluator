from pydantic import BaseModel


class StockData(BaseModel):

    ticker: str

    current_price: float | None = None

    fifty_two_week_high: float | None = None

    fifty_two_week_low: float | None = None

    volume: int | None = None

    average_volume: int | None = None