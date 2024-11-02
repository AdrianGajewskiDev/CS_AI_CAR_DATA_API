from pydantic import BaseModel
from typing import List

class History(BaseModel):
    first_owner: List[str]
    first_owner_from_new: List[str]
    accident_free: List[str]
    registered_in_poland: List[str]
    serviced_at_authorized_service_center: List[str]
    registered_as_a_vintage_car: List[str]
    tuning: List[str]
    truck_homologation: List[str]
    warranty: List[str]