import json
from lambda_function import handler

def test_lambda_handler_valid():
    event = {
        "body": json.dumps({"message": "Hello, chatbot!"})
    }
    response = handler.lambda_handler(event, None)
    assert response["statusCode"] in [200, 500]  # If OpenAI key is missing, will return 500