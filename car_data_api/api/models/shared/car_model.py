from typing import List, Optional
from pydantic import BaseModel

class ModelGeneration(BaseModel):
    generation: str

class Model(BaseModel):
    model: str