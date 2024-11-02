import json
import os
from car_data_api.api.models.response.car_details_response_model import CarDetailsResponseModel


def get_car_equipment_details_response() -> CarDetailsResponseModel:
    lambda_root = os.environ["LAMBDA_TASK_ROOT"]
    with open(f"{lambda_root}/car_data_api/api/static_files/tech_data.json", "r") as file:
        tech_data = json.load(file)

    with open(f"{lambda_root}/car_data_api/api/static_files/equipment.json", "r") as file:
        equipment = json.load(file)

    with open(f"{lambda_root}/car_data_api/api/static_files/history.json", "r") as file:
        history = json.load(file)

    with open(f"{lambda_root}/car_data_api/api/static_files/sell_options.json", "r") as file:
        sell_options = json.load(file)

    with open(f"{lambda_root}/car_data_api/api/static_files/body_types.json", "r") as file:
        body_types = json.load(file)

    with open(f"{lambda_root}/car_data_api/api/static_files/car_color.json", "r") as file:
        colors = json.load(file)

    return CarDetailsResponseModel(tech_data=tech_data, equipment=equipment, history=history, sell_options=sell_options, body_types=body_types, colors=colors)