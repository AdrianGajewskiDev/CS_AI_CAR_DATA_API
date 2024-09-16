from pydantic import BaseModel


class StaticDataResponseModel(BaseModel):
    transmissions: list[dict]
    fuel_types: list[dict]