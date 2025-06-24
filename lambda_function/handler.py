import json
import os
import openai

# Get OpenAI API Key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        user_message = body.get("message", "")

        if not user_message:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'message' in request"})
            }

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        reply = response.choices[0].message.content

        return {
            "statusCode": 200,
            "body": json.dumps({"reply": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
