import sys
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    return f"Hello, {who_to_greet}"


r = requests.get("https://google.com")
print(r.status_code)
