from fastapi import HTTPException
from car_data_api.api.clients.db_client import DbClient
from cs_ai_common.logging.internal_logger import InternalLogger
from car_data_api.api.models.response.generations_response_model import GenerationsResponseModel
import ast

def get_generations_response(make: str, model: str, db_client: DbClient) -> GenerationsResponseModel:
    db_response = db_client.get_generations(make, model)

    if not db_response or len(db_response) == 0:
        raise HTTPException(status_code=404, detail="Generations not found")
    
    model = db_response[0]
    InternalLogger.LogInfo("Model: " + str(model))
    generations = ast.literal_eval(model["generations"])

    return GenerationsResponseModel(generations=generations, total_count=len(generations))