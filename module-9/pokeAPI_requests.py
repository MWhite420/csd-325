#Mark White
#CSD325
#Assignment9.2

import requests
response = requests.get('https://pokeapi.co/api/v2/generation/?offset=2&limit=2')
print(response.status_code)
print(response.json())