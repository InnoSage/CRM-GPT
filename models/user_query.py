from pydantic import BaseModel


class UserQuery(BaseModel):
    question: str
    attributesNames: list
