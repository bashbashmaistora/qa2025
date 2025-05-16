import pytest
from utils import post_request
import json

with open("config.json") as config_file:
    config = json.load(config_file)

BASE_URL = config["base_url"]

def test_successful_registration():
    payload = {
        "email": "user@example.com",
        "confirmEmail": "user@example.com",
        "password": "Password123"
    }
    response = post_request(BASE_URL, payload)
    assert response.status_code == 200
    assert response.json()["success"] == True

def test_email_too_long():
    payload = {
        "email": "a" * 26 + "@example.com",
        "confirmEmail": "a" * 26 + "@example.com",
        "password": "Password123"
    }
    response = post_request(BASE_URL, payload)
    assert response.status_code == 400
    assert "Email must not exceed 25 characters" in response.json()["errors"]["email"]

def test_password_without_capital():
    payload = {
        "email": "user@example.com",
        "confirmEmail": "user@example.com",
        "password": "password123"
    }
    response = post_request(BASE_URL, payload)
    assert response.status_code == 400
    assert "Password must contain at least one capital letter" in response.json()["errors"]["password"]

def test_sql_injection():
    payload = {
        "email": "' OR 1=1; --",
        "confirmEmail": "' OR 1=1; --",
        "password": "Password123"
    }
    response = post_request(BASE_URL, payload)
    assert response.status_code == 400

def test_xss_injection():
    payload = {
        "email": "<script>alert(1)</script>",
        "confirmEmail": "<script>alert(1)</script>",
        "password": "Password123"
    }
    response = post_request(BASE_URL, payload)
    assert response.status_code == 400

