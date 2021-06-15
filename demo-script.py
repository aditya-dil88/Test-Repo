import requests


r = requests.get("https://google.com")
print(r.headers)
print(r.status_code)
