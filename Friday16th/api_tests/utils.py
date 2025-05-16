import requests
import json

def post_request(endpoint, payload):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    return response

def load_test_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

