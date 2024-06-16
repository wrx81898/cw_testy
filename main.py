import requests
import json


def check_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"HTTP Status: 200 OK")
            return check_json(response.json())
        else:
            print(f"HTTP Status: {response.status_code}")
            return "FAILED"
    except Exception as e:
        print(f"Exception occurred: {e}")
        return "FAILED"


def check_json(body):
    try:
        required_keys = ['id', 'title']
        for key in required_keys:
            if key not in body:
                return "FAILED"
        return "PASSED"
    except json.JSONDecodeError:
        print("Failed to parse JSON")
        return "FAILED"


# Lista endpointów API do przetestowania
endpoints = [
    'https://my-json-server.typicode.com/typicode/demo/posts/1',
    'https://my-json-server.typicode.com/typicode/demo/posts/2',
    'https://my-json-server.typicode.com/typicode/demo/posts/3'
]

# Testowanie każdego endpointu
for i, endpoint in enumerate(endpoints):
    print(f"Testing endpoint {i + 1} ({endpoint}):")
    result = check_response(endpoint)
    print(f"Test {i + 1}: {result}\n")
