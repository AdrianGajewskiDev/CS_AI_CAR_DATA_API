from pydantic import BaseModel

from car_data_api.api.models.shared.body_types import BodyTypes
from car_data_api.api.models.shared.colors import Colors
from car_data_api.api.models.shared.equipment import Equipment
from car_data_api.api.models.shared.history import History
from car_data_api.api.models.shared.sell_options import SellOptions
from car_data_api.api.models.shared.tech_data import TechData

class CarDetailsResponseModel(BaseModel):
    tech_data: TechData
    equipment: Equipment
    history: History
    sell_options: SellOptions
    body_types: BodyTypes
    colors: Colors