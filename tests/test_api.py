import pytest
import requests
import allure
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestAPI:
    @allure.step("Check HTTP status code of the main page")
    def test_status_code(self):
        response = requests.get(Links.HOST)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    @allure.step("Verify Content-Type header of the main page response")
    def test_content_type(self):
        response = requests.get(Links.HOST)
        assert response.headers['Content-Type'].startswith(
            'text/html'), f"Expected content type to start with 'text/html' but got {response.headers['Content-Type']}"

    @allure.step("Verify that login button is present and clickable")
    def test_login_button_present_and_clickable(self):
        self.driver.get(Links.HOST)

        login_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        assert login_button.is_displayed(), "Login button is not displayed"
        assert login_button.is_enabled(), "Login button is not enabled"

        login_button.click()
        WebDriverWait(self.driver, 15).until(
            EC.url_changes(Links.HOST)
        )
        assert self.driver.current_url == Links.LOGIN_PAGE, \
            "URL did not change as expected after clicking the login button"