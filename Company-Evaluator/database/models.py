from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.base import Base


class Company(Base):

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    ticker: Mapped[str] = mapped_column(
        String(20)
    )

    name: Mapped[str] = mapped_column(
        String(255)
    )