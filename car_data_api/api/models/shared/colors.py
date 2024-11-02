from pydantic import BaseModel
from typing import List

class Colors(BaseModel):
    car_colors: List[str]