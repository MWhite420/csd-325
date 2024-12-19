#Mark White
#CSD325
#Assignment9.2

import requests
import json
response = requests.get('http://api.open-notify.org/astros')

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(response.status_code)
jprint(response.json())