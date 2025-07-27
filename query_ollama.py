import requests


ollama_URL = "http://localhost:11434/api/generate"


def query_ollama(prompt, model="llama3.2"):
    response = requests.post(ollama_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    if response.status_code == 200:
        return response.json()["response"]
