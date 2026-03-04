import pandas as pd
import json
df = pd.read_csv(r"C:\Users\piyal\OneDrive\Desktop\Learning\Python\python_practice_room\questions\question_06\data.csv")

parsed = df["json_data"].apply(json.loads)
tmp = pd.json_normalize(parsed)
print(tmp.head())

tmp["timestamp"] = pd.to_datetime(tmp["timestamp"], errors="coerce")
print(tmp.head())
tmp["hour"] = tmp["timestamp"].dt.hour
tmp["min"] = tmp["timestamp"].dt.minute

print(tmp.head())