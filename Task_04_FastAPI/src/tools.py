from pydantic import BaseModel


class Message(BaseModel):
    text: str


class SignedMessage(BaseModel):
    text: str
    signature: str
