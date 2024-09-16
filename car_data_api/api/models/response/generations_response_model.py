from typing import List

from pydantic import BaseModel

from car_data_api.api.models.shared.car_model import ModelGeneration


class GenerationsResponseModel(BaseModel):
    generations: List[ModelGeneration]
    total_count: int