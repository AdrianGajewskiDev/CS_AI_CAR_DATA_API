from typing import List

from pydantic import BaseModel

class GenerationsResponseModel(BaseModel):
    generations: List[str]
    total_count: int