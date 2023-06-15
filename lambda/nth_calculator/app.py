from algorithm import calculate_yellowstone_permutation_integer
import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NthCalculatorDatabase')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):

    response = table.get_item(
        Key={
            'ID': 'memoised_sequence'
        }
    )

    calculation_args = [int(event['n'])]

    if 'Item' in response:
        item = response['Item']
        if 'as_python_list' in item:
            memoised_sequence = item['as_python_list']
            calculation_args.append(memoised_sequence)

    # NOTE: n = 1 corresponds to first element in sequence
    yellowstone_integer, memoised_sequence = calculate_yellowstone_permutation_integer(*calculation_args)

    _ = table.put_item(
        Item={
            'ID': 'memoised_sequence',
            'as_python_list': memoised_sequence,
            'LatestGreetingTime': now
        }
    )
    
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(yellowstone_integer))
    }