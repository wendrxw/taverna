from pydantic import BaseModel


class RollRequest(BaseModel):
    expression: str