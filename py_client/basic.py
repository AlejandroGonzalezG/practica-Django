import requests

# endpoint = "https://httpbin.org//status/200/"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "Hello World"})
print(get_response.json())