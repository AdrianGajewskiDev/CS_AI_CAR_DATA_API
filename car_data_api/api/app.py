import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from car_data_api.api.middleware.catch_exceptions_middleware import catch_exceptions_middleware
from car_data_api.api.endpoints.car_data_endpoints import car_data_router

app = FastAPI()

origins: list[str] = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3031",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(catch_exceptions_middleware)

app.include_router(car_data_router, tags=["car-data-endpoints"])