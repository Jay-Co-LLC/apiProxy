import json
import boto3

lambda_client = boto3.client('lambda')

def lambda_handler(event, context):
    
    name = event['queryStringParameters']['name']
    
    lambda_client.invoke(
        FunctionName='getFullData',
        InvocationType='Event',
        Payload=json.dumps({'name' : name}))
    
    # TODO implement
    return {
        'statusCode': 202,
        'body': json.dumps('Function invoked successfully! Processing...')
    }
