from pydantic import BaseModel


class AgentResult(BaseModel):

    title: str

    summary: str

    key_points: list[str]