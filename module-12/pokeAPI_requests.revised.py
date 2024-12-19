#Mark White
#CSD325
#Assignment9.2

import json
import requests
response = requests.get('https://pokeapi.co/api/v2/generation/?offset=2&limit=2')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(response.status_code)
jprint(response.json())