import json
import pandas as pd


def cleanData(data):
    with open("enrichedData/enrichedData.json", 'w') as f:
        json.dump(data, f, indent=4)

    dataFrame = pd.DataFrame(data)
    dataFrame.to_excel("enrichedData/enriched_data.xlsx", index=False)
