from pydantic import BaseModel
from typing import List

class HistoryNested(BaseModel):
    origin: List[str]

class History(BaseModel):
    checks: List[str]
    nested: HistoryNested