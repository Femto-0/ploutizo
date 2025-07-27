import requests

ollama_URL = "http://localhost:11434/api/generate"
prompt = "process the given string and return a json response such in the format: <first_name>, <last_name>, <name> and <organization_name>"


def query_ollama(prompt, model="llama3.2"):
    details = []
    response = requests.post(ollama_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        for item in response:
            dict = {
                'first_name': item['first_name'],
                'last_name': item['last_name'],
                'name': item['name'],
                'organization_name': item['organization_name']
            }
            details.append(dict)
        return details
    else:
        print("faulty req to" + {model})
