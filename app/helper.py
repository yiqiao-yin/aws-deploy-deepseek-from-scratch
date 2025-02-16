import requests
import json

# API Gateway Invoke URL (Replace with your actual API endpoint)
API_URL = "https://zyqnod20re.execute-api.us-east-1.amazonaws.com/dev/test_bedrock_v4_deepseek"

def query_deepseek(prompt: str, max_gen_len: int, temperature: float, top_p: float) -> str:
    """
    Sends a request to the DeepSeek-R1 model via AWS Bedrock API and returns the response.
    
    Args:
        prompt (str): The user input query.
        max_gen_len (int): The maximum length of the generated response.
        temperature (float): Controls the randomness of the model output.
        top_p (float): The nucleus sampling parameter.

    Returns:
        str: The generated response from the model.
    """
    payload = {
        "prompt": prompt,
        "max_gen_len": max_gen_len,
        "temperature": temperature,
        "top_p": top_p
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            full_response = response.json()
            
            # Extract the output text from the model response
            output_text = full_response.get("model_response", {}).get("generation", "No output found.")
            return output_text
        else:
            return f"Error {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"