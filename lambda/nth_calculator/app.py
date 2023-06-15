from algorithm import calculate_yellowstone_permutation_integer
import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NthCalculatorDatabase')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):

    # NOTE: n = 1 corresponds to first element in sequence
    yellowstone_integer, _ = calculate_yellowstone_permutation_integer(int(event['n']))
    response = table.put_item(
        Item={
            'ID': str(yellowstone_integer),
            'LatestGreetingTime':now
        }
    )
    
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(yellowstone_integer))
    }