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
            "factorTurnover": params["factorTurnover"],
            "factorAPR": params["factorAPR"],
            "tickerMap": params["tickerMap"],
            "minShareLP": params["minShareLP"],
            "marketActive": params["marketActive"]
        }
    })

    return response

print(lambda_handler(0,0))
