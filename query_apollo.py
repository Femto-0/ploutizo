import os
import requests


def query_apollo(list):
    apiKey = os.environ['APOLLO_API']
    url = "https://api.apollo.io/api/v1/people/bulk_match?reveal_personal_emails=true"
    payload = list
    headers = {
        "accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Api-key": apiKey
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
