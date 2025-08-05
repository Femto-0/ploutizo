import json
# import pandas as pd


def extract_relevant_data(raw_data):

    cleanedData = []

    for item in raw_data:
        if not isinstance(item, dict):
            continue
        
        first_name = item.get("first_name")
        last_name = item.get("last_name")
        linkedin_url = item.get("linkedin_url")
        title = item.get("title")
        email = item.get("email")

        employment_history = item.get("employment_history", [])
        if employment_history:
            most_recent_job = employment_history[0]
            job_info = {
                "organization_name": most_recent_job.get("organization_name"),
                "title": most_recent_job.get("title")
            }
            filtered_employment_history = [job_info]
        else:
            filtered_employment_history = []

        filtered_detail = {
            "first_name": first_name,
            "last_name": last_name,
            "linkedin_url": linkedin_url,
            "title": title,
            "email": email,
            "employment_history": filtered_employment_history
        }

        cleanedData.append(filtered_detail)

    return cleanedData


def cleanData(raw_data, imageId):
    # to make sure that raw_data I am supplying is a dict and not a list
    print(f"raw data type: {type(raw_data)}")
    # Save raw data to JSON file for inspection/debugging
    data = extract_relevant_data(raw_data)
    print(data)
    with open(f"enrichedData/{imageId}_enrichedData.json", 'w') as f:
        json.dump(data, f, indent=4)
