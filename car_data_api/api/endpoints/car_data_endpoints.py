from typing import Annotated
from fastapi import APIRouter, Depends

from car_data_api.api.clients.db_client import DbClient
from car_data_api.api.dependencies.db_client_dependency import DynamoDbClient
from car_data_api.api.models.response.generations_response_model import GenerationsResponseModel
from car_data_api.api.models.response.makes_response_model import MakesResponseModel
from car_data_api.api.models.response.models_response_model import ModelsResponseModel
from car_data_api.api.responses.get_generations_response import get_generations_response
from car_data_api.api.responses.get_models_response import get_models_response
from car_data_api.api.responses.get_makes_response import get_makes_response

car_data_router = APIRouter(prefix="/car-data", tags=["car-data-endpoints"])

@car_data_router.get("/get-makes", status_code=200, response_model=MakesResponseModel)
def get_makes():
    return get_makes_response()


@car_data_router.get("/get-models", status_code=200, response_model=ModelsResponseModel)
def get_models(make: str, db_client: Annotated[DbClient, Depends(DynamoDbClient)]):
    return get_models_response(make, db_client)


@car_data_router.get("/get-generations", status_code=200, response_model=GenerationsResponseModel)
def get_generations(make: str, model: str, db_client: Annotated[DbClient, Depends(DynamoDbClient)]):
    return get_generations_response(make, model, db_client)