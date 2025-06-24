# GenAI Chatbot using OpenAI + AWS Lambda

This is a serverless GenAI chatbot using Python, OpenAI GPT API, AWS Lambda, and API Gateway.

## 💡 How it works

- User sends a POST request with a message to an API Gateway endpoint.
- The request triggers a Lambda function.
- Lambda sends the message to OpenAI GPT API.
- GPT responds, and the reply is returned to the user.

## 🛠️ Technologies Used

- Python
- OpenAI GPT (via `openai` library)
- AWS Lambda (serverless compute)
- AWS API Gateway (REST endpoint)

## 🔐 Setup

1. Set `OPENAI_API_KEY` in Lambda environment variables.
2. Install Python libraries and zip the deployment package:
   ```bash
   pip install -r requirements.txt -t package/
   cp -r lambda_function/* package/
   cd package && zip -r chatbot.zip .
