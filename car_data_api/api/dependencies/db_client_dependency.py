from datetime import datetime
import os

import boto3
from boto3.dynamodb.conditions import Key
from car_data_api.api.clients.db_client import DbClient

class DynamoDbClient(DbClient):
    table_name: str
    def __init__(self):
        self.table_name = os.getenv('CAR_DATA_TABLE_NAME')
    
    def get_makes(self, make: str) -> dict:
        dynamodb_resource = boto3.resource('dynamodb')
        table = dynamodb_resource.Table(self.table_name)
        filtering_exp = Key('make').eq(make)
        return table.query(KeyConditionExpression=filtering_exp)['Items']

    def get_generations(self, make: str, model: str) -> dict:
        dynamodb_resource = boto3.resource('dynamodb')
        table = dynamodb_resource.Table(self.table_name)
        filtering_exp = Key('make').eq(make) & Key('model').eq(model)
        return table.query(KeyConditionExpression=filtering_exp)['Items']