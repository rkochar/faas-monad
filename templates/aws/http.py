import json
import boto3


def template(event, context):
    query_string_parameters = event.get("queryStringParameters") or {}
    headers = event.get("headers") or {}

    body = ""

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }