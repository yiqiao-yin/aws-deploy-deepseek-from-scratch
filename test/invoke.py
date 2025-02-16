import requests
import json

# API Gateway Invoke URL (Replace with your actual URL)
API_URL = "https://zyqnod20re.execute-api.us-east-1.amazonaws.com/dev/test_bedrock_v4_deepseek"

# Define the payload
payload = {
    "prompt": "What is 1+1? Is it 2? Is it an assumption? If yes, why can't 1+1=0?",  # The input text/question for the AI model to generate a response.
    
    "max_gen_len": 1024,  # The maximum number of tokens (words/subwords) the model can generate in the response.
    
    "temperature": 0.1,  # Controls randomness in response generation. 
                         # Lower values (e.g., 0.1) make the output more deterministic and repetitive, 
                         # while higher values (e.g., 1.0) make responses more diverse and creative.

    "top_p": 0.9  # Implements nucleus sampling: instead of sampling from the full probability distribution, 
                  # the model considers only the top `p` probability mass. 
                  # A lower value (e.g., 0.5) makes responses more conservative, 
                  # while a higher value (e.g., 0.95) makes them more diverse.
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
