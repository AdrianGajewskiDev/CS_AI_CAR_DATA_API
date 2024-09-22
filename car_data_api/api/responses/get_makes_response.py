from car_data_api.api.models.response.makes_response_model import MakesResponseModel
from fastapi import HTTPException
def get_makes() -> list[str]:
    return ["Toyota", "Bmw", "Audi", "Mercedes-Benz"]

def get_makes_response() -> MakesResponseModel:
    makes = get_makes()
    if not makes:
        raise HTTPException(status_code=404, detail="Makes not found")
    return MakesResponseModel(makes=makes, total_count=len(makes))