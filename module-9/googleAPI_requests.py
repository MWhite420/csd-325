#Mark White
#CSD325
#Assignment9.2

import requests
import json
response = requests.get("http://api.open-notify.org/astros")
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())