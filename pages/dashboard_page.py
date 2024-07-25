import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    CLAIM_BUTTON = ("xpath", "//span[text()='Claim']")

    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()

    @allure.step("Click on 'Claim' link")
    def click_claim_link(self):
        self.wait.until(EC.element_to_be_clickable(self.CLAIM_BUTTON)).click()