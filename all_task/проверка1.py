import requests

url = "https://cs-sexy.ru/"

req = requests.get(url)

print(req.text)
