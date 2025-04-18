from pydantic import BaseModel
from typing import Optional

class Mission(BaseModel):
    id: int
    name: str
    launch_date: str
    budget: float
    crew: int
    status: str
