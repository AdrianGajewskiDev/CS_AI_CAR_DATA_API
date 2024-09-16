import json
from typing import List
from fastapi import HTTPException
from car_data_api.api.clients.db_client import DbClient
from car_data_api.api.models.response.generations_response_model import GenerationsResponseModel
from car_data_api.api.models.shared.car_model import ModelGeneration


def get_generations_response(make: str, model: str, db_client: DbClient) -> GenerationsResponseModel:
    db_response = db_client.get_generations(make, model)

    if not db_response or len(db_response) == 0:
        raise HTTPException(status_code=404, detail="Generations not found")
    
    model = db_response[0]
    generations = _build_generations(json.loads(model["generations"]))

    return GenerationsResponseModel(generations=generations, total_count=len(generations))

def _build_generations(db_response: list[dict]) -> list[ModelGeneration]:
    generations: List[ModelGeneration] = []
    for item in db_response:
        _gen = ModelGeneration(
            generation=item['model'],
            years=item['years'],
        )
        _gen._map_years()
        generations.append(_gen)
    return generations