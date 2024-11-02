from pydantic import BaseModel
from typing import List

class BodyTypes(BaseModel):
    body_types: List[str]