from mangum import Mangum

from car_data_api.api.app import app

def handler(event, context):
    mangum_handler = Mangum(app)
    return mangum_handler(event, context)