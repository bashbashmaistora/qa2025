import requests
from utils.config import API_ENDPOINT, HEADERS
from utils.data_provider import get_valid_data, get_invalid_email_data

def test_valid_registration():
    response = requests.post(API_ENDPOINT, json=get_valid_data(), headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_invalid_email_format():
    response = requests.post(API_ENDPOINT, json=get_invalid_email_data(), headers=HEADERS)
    assert response.status_code == 400
    assert "Email must not exceed 25 characters" in response.json()["errors"]["email"]

