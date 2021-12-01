import json
import requests

url = str("https://api.alternative.me/fng/")

fgIndexJson = requests.get(url)

jsonData = fgIndexJson.json()

lastFGIndexValue = jsonData["data"][0]["value"]

print(lastFGIndexValue)






"""
jsonData = requests.get(str("https://api.alternative.me/fng/")).json()
"""