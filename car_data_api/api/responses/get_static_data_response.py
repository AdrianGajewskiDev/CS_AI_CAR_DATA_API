import json
import os
from car_data_api.api.models.response.static_data_response_model import StaticDataResponseModel


def get_static_data_response() -> StaticDataResponseModel:
    return StaticDataResponseModel(transmissions=[_dict for _dict in load_from_file("transmissions")], fuel_types=[_dict for _dict in load_from_file("fuel_types")])

def load_from_file(file_name: str) -> list[dict]:
    path = os.environ["LAMBDA_TASK_ROOT"] + f"/car_data_api/api/static_files/{file_name}.json"
    with open(path, "r") as file:
        return json.load(file)