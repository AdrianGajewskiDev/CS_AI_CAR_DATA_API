from typing import List

from pydantic import BaseModel


class ModelsResponseModel(BaseModel):
    models: List[str]
    total_count: int