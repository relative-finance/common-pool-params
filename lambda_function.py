import json

with open("params.json") as file:
    params = json.load(file)

def lambda_handler(event, context):
    try:
        response = json.dumps({
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": {
                "factorTurnover": params["factorTurnover"],
                "factorAPR": params["factorAPR"],
                "minTradeValueBp": params["minTradeValueBp"],
                "swapSlipPct": params["swapSlipPct"],
                "tickerMap": params["tickerMap"],
                "minShareLP": params["minShareLP"],
                "marketActive": params["marketActive"]
            }
        })
        return response
    except:
        error_response = json.dumps({
            "statusCode": 404
        })
        return error_response
