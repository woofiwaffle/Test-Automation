import allure
import pytest
from base.base_claim_test import BaseClaimTest

@allure.feature("Claim Functionality")
class TestClaimFeature(BaseClaimTest):
    @allure.title("Get claim data")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_claim_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()

        self.dashboard_page.is_opened()
        self.dashboard_page.click_claim_link()

        self.claim_page.is_opened()
        self.claim_page.enter_reference_id()
        self.claim_page.submit_search()
        self.claim_page.is_search_saved()

        self.claim_page.make_screenshot("ClaimInfo_Success")

        csv_file_path = "received_data/claim_info.csv"
        self.claim_page.save_claim_info_to_csv(csv_file_path)

