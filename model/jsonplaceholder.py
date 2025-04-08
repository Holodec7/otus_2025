from pydantic import BaseModel, Field, EmailStr


class Posts(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Albums(BaseModel):
    userId: int
    id: int
    title: str
