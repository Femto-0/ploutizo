import os
import requests
import json


def query_apollo(people_list):
    apiKey = os.environ.get('APOLLO_API')
    print(apiKey)
    if not apiKey:
        raise ValueError("Missing apollo api key")
    else:
        url = "https://api.apollo.io/api/v1/people/bulk_match?reveal_personal_emails=true"
        payload = {
            'details': people_list
        }
        print(json.dumps(payload, indent=2))

        headers = {
            "accept": "application/json",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "x-api-key": apiKey
        }
        response = requests.post(url, json=payload, headers=headers)
        if (response.status_code == 200):
            data = response.json()
            print(json.dumps(data, indent=4))
