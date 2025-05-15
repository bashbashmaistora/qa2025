from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_successful_form_submission(driver):
    driver.get("https://abc13514.sg-host.com/")
    driver.find_element(By.NAME, "email").send_keys("user@example.com")
    driver.find_element(By.NAME, "confirmEmail").send_keys("user@example.com")
    driver.find_element(By.NAME, "password").send_keys("Password123")
    driver.find_element(By.NAME, "submit").click()
    success_message = driver.find_element(By.ID, "message").text
    assert "Registration successful" in success_message

