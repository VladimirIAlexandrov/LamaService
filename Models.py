from dataclasses import dataclass
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class MessageType(str, Enum):
    USER = "user"
    AI = "AI"


class User(BaseModel):
    id: str
    name: str
    avatar: str

class Message(BaseModel):
    id: str
    message: str
    userId: str
    groupId: str
    messageType: MessageType
    AiRepliedId: Optional[str]
    created: int
    user: User

class Answer(BaseModel):
    answer: str
    messageId: str
    created: int
