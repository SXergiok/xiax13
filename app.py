def lambda_handler(event, context):
    params=event.get('queryStringParameters')
    a=params.get('a')
    b=params.get('b')
    c=int(a)+int(b)
        # TODO implement
    return {
        'statusCode': 200,
        'body': c
    }
