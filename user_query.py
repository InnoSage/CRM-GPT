from pydantic import BaseModel


class UserQuery(BaseModel):
    question: str
    attributes_names: list
