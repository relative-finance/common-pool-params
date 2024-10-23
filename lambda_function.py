import json

with open("params.json") as file:
    params = json.load(file)

def lambda_handler(event, context):

    response = json.dumps({
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "MinShareLP": params["MinShareLP"],
            "MarketActive": params["MarketActive"]
        }
    })

    return response

print(lambda_handler(0,0))
