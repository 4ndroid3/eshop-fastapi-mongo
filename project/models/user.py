from pydantic import BaseModel

class User(BaseModel):
    _id: str | None = None
    name:str
    email:str
    password:str