import requests
import pandas as pd

jsonData = requests.get("https://api.alternative.me/fng/").json()
df = pd.DataFrame.from_dict(jsonData['data'])

print(df["value"][0])