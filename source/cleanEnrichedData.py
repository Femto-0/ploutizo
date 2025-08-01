import json
import pandas as pd


def cleanData(data, imageId):
    # Save raw data to JSON file for inspection/debugging
    with open(f"enrichedData/{imageId}_enrichedData.json", 'w') as f:
        json.dump(data, f, indent=4)

    # Check if data is a list
    if not isinstance(data, list):
        print("Warning: data is not a list. Attempting to convert it into a list.")
        data = [data]

    # Filter out any items that are not dictionaries or are None
    cleaned_data = [item for item in data if isinstance(item, dict)]

    if not cleaned_data:
        print("Error: No valid dictionary entries found in data to convert to DataFrame.")
        return

    # Create DataFrame and save to Excel
    dataFrame = pd.DataFrame(cleaned_data)
    dataFrame.to_excel(
        f"enrichedData/{imageId}_enriched_data.xlsx", index=False)
    print(f"Data saved to {imageId}_enriched_data.xlsx")
