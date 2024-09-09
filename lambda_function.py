import json

def lambda_handler(event, context):
    # TODO implement
    print("hello priyam!!!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! form linux world!! ')
    }
