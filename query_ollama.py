import requests
import json

ollama_URL = "http://localhost:11434/api/generate"


def query_ollama(image_to_String, model):
    prompt = f"""
Extract relevant information from the following text and return a JSON array of objects with the following fields: first_name, last_name, name(combine first and last name), and organization_name.

Text:
{image_to_String}

Respond only with the JSON containing the response.
"""
    response = requests.post(ollama_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        data = json.loads(response.text)['response']
        parsed_data = json.loads(data)
        print(parsed_data)
        return parsed_data
    else:
        print("faulty req to" + model)
