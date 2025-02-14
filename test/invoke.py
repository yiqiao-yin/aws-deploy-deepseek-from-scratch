import requests
import json

# API Gateway Invoke URL (Replace with your actual URL)
API_URL = "https://zyqnod20re.execute-api.us-east-1.amazonaws.com/dev/test_bedrock_v4_deepseek"

# Define the payload
payload = {
    "prompt": "what is 1+1?",
    "max_gen_len": 1024,
    "temperature": 0.5,
    "top_p": 0.9
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Send POST request
try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    # Check if the response was successful
    if response.status_code == 200:
        full_response = response.json()

        # Save full response to a file
        with open("bedrock_response.json", "w") as f:
            json.dump(full_response, f, indent=2)

        # Extract the output text from model response
        output_text = full_response.get("model_response", {}).get("generation", "No output found.")

        # Print only the output text
        print("\nExtracted Output Text:\n", output_text)

    else:
        print(f"Error {response.status_code}: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
