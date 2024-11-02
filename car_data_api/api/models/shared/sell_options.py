from pydantic import BaseModel
from typing import List

class SellOptions(BaseModel):
    sell_options: List[str]