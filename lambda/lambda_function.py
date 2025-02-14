import boto3
import json

# Initialize AWS Bedrock Runtime client
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

# Model ARN (Replace with your actual model ARN)
MODEL_ARN = "arn:aws:bedrock:us-east-1:141273913934:imported-model/pg6s1qosvls9"

def lambda_handler(event, context):
    """
    AWS Lambda function to invoke an imported Bedrock model.
    Allows users to specify max_gen_len, temperature, and top_p.
    """

    # DEBUG: Print event to check incoming request
    print("Received event:", json.dumps(event, indent=2))

    # Extract request body (handling API Gateway string-wrapped JSON)
    try:
        if isinstance(event.get("body"), str):
            body = json.loads(event["body"])
        else:
            body = event.get("body", {})

        # Extract prompt and optional parameters with defaults
        prompt = body.get("prompt", "Tell me a joke.")
        max_gen_len = body.get("max_gen_len", 512)
        temperature = body.get("temperature", 0.5)
        top_p = body.get("top_p", 0.9)

    except (json.JSONDecodeError, TypeError):
        # Handle cases where JSON is malformed
        prompt = "Tell me a joke."
        max_gen_len = 512
        temperature = 0.5
        top_p = 0.9

    # Construct the Bedrock API request body
    model_body = json.dumps({
        "prompt": prompt,
        "max_gen_len": max_gen_len,
        "temperature": temperature,
        "top_p": top_p
    })

    kwargs = {
        "modelId": MODEL_ARN,
        "contentType": "application/json",
        "accept": "application/json",
        "body": model_body
    }

    try:
        # Invoke the Bedrock model
        resp = bedrock_runtime.invoke_model(**kwargs)
        resp_json = json.loads(resp["body"].read().decode("utf-8"))

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Bedrock Model Response",
                "input_prompt": prompt,
                "parameters_used": {
                    "max_gen_len": max_gen_len,
                    "temperature": temperature,
                    "top_p": top_p
                },
                "model_response": resp_json
            }, indent=2)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
