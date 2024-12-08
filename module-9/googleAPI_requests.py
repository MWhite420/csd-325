#Mark White
#CSD325
#Assignment9.2


import requests
response = requests.get('http://api.open-notify.org/astros')
print(response.status_code)
print(response.json())