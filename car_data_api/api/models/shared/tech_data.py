from pydantic import BaseModel
from typing import List, Dict

class ElectricNested(BaseModel):
    battery_ownership: List[str]

class Electric(BaseModel):
    text: List[str]
    nested: ElectricNested

class TechData(BaseModel):
    steering_wheel: List[str]
    drive: List[str]
    color_type: List[str]
    number_of_seats: List[str]
    electric: Electric