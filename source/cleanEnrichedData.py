import json
import pandas as pd
from pandas import json_normalize


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

        # Employment history
        employment_history = item.get("employment_history", [])
        filtered_employment_history = []

        if employment_history and isinstance(employment_history, list):
            most_recent_job = employment_history[0] if len(
                employment_history) > 0 else {}
            last_job = employment_history[1] if len(
                employment_history) > 1 else {}

            job_info = {
                "organization_name": most_recent_job.get("organization_name"),
                "last_job": last_job.get("organization_name"),
                "last_job_title": last_job.get("title")
            }

            filtered_employment_history.append(job_info)

        # Add to cleaned data
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


def cleanData(processed_data, imageId):
    data_frame = pd.json_normalize(
        processed_data,
        meta=['first_name', 'last_name', 'linkedin_url', 'title', 'email'],
        record_path='employment_history',
        errors='ignore'
    )

    data_frame_reindexed_cols = data_frame.reindex(
        columns=[
            'first_name',
            'last_name',
            'linkedin_url',
            'organization_name',
            'title',
            'email',
            'last_job',
            'last_job_title'])
    file_name = f"{imageId}"
    data_frame_reindexed_cols.to_excel(
        f"enrichedData/{file_name}.xlsx", index=False)
    print(f"saved as {file_name}.xlsx in dir: enrichedData")

    records = data_frame_reindexed_cols.to_dict(orient="records")
    with open(f"enrichedData/{imageId}_enrichedData.json", 'w') as f:
        json.dump(records, f, indent=4)
    print(f"saved as {file_name}_enrichedData.json in dir: enrichedData")
