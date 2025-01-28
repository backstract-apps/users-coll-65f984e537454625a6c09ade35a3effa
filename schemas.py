from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


class ReadUser(BaseModel):
    id: int
    first_name: str
    last_name: str
    class Config:
        from_attributes = True




class PostUser(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True



class PutUserId(BaseModel):
    id: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True

