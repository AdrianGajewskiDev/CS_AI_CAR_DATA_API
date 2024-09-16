from typing import List

from pydantic import BaseModel


class MakesResponseModel(BaseModel):
    makes: List[str]
    total_count: int