import pytest
from utils import post_request, load_test_data

# Load the test data from the JSON file
test_data = load_test_data("test_data.json")

@pytest.mark.parametrize("data", test_data)
def test_registration(data):
    payload = {
        "email": data["email"],
        "confirmEmail": data["confirmEmail"],
        "password": data["password"]
    }
    response = post_request("https://abc13514.sg-host.com/api.php", payload)

    # Assert status code
    assert response.status_code == data["expected_status"], (
        f"Test '{data['description']}' failed: Expected status {data['expected_status']}, got {response.status_code}. Response: {response.text}"
    )

    # Assert expected message if present
    if "expected_message" in data:
        resp_json = response.json()
        actual_message = resp_json.get("message", "")

        if data["expected_message"] == "Validation failed":
            # If the expected message is exactly "Validation failed", just check it matches the actual message
            assert "Validation failed" in actual_message, (
                f"Test '{data['description']}' failed: Expected message containing 'Validation failed', got '{actual_message}'."
            )
        elif actual_message == "Validation failed":
            # If actual message says validation failed, check errors for expected message substring
            error_messages = [msg for msg in resp_json.get("errors", {}).values()]
            assert any(data["expected_message"] in msg for msg in error_messages), (
                f"Test '{data['description']}' failed: Expected message '{data['expected_message']}', got '{actual_message}' and errors {error_messages}."
            )
        else:
            # Otherwise, just check expected message is in the actual message
            assert data["expected_message"] in actual_message, (
                f"Test '{data['description']}' failed: Expected message '{data['expected_message']}', got '{actual_message}'."
            )

