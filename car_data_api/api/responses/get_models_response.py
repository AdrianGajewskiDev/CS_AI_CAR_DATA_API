import json
from typing import List
from fastapi import HTTPException
from car_data_api.api.clients.db_client import DbClient
from car_data_api.api.models.response.models_response_model import ModelsResponseModel
from car_data_api.api.models.shared.car_model import Model, ModelGeneration


def get_models_response(make: str, db_client: DbClient) -> ModelsResponseModel:
    db_response = db_client.get_makes(make)

    if not db_response or len(db_response) == 0:
        raise HTTPException(status_code=404, detail="Models not found")
    
    models = [item['model'] for item in db_response]

    return ModelsResponseModel(models=models, total_count=len(models))