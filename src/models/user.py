from pydantic import BaseModel
from typing import List

class User(BaseModel):
    full_name: str
    email: str
    role: List[str]
    organization: str