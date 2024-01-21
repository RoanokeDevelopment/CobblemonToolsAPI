import requests
import json
import pprint

pp = pprint.PrettyPrinter(depth=5)
url = "https://cobblemon.tools/api/v1/pokedex/search"

request = {
    "types": ["fire"],
    "implemented": True,
    "ev_yields": ["defence"]
}

response = requests.post(url, json=request)

if response.status_code != 200:
    print("Error getting data from API!")
    exit(0)

results = json.loads(response.text)
pp.pprint(results)
