import allure
import csv
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ClaimPage(BasePage):
    PAGE_URL = Links.CLAIM_PAGE

    REFERENCE_ID_INPUT = (By.XPATH, '(//input[@placeholder="Type for hints..."])[2]')
    SEARCH_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]')
    CLAIM_INFO = (By.XPATH, '(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]')
    NUMBER_EXTRACTOR = (By.XPATH, '(//div[@data-v-6c07a142])[1]')
    SPINNER = (By.XPATH, '//div[@class="oxd-loading-spinner"]')


    @allure.step("Get and Enter Reference ID")
    def enter_reference_id(self):
        number_element = self.wait.until(EC.presence_of_element_located(self.NUMBER_EXTRACTOR))
        number_text = number_element.text.strip()

        reference_id_field = self.wait.until(EC.element_to_be_clickable(self.REFERENCE_ID_INPUT))
        reference_id_field.clear()
        reference_id_field.send_keys(number_text)

    @allure.step("Press the search button")
    def submit_search(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Get claim information")
    def get_claim_info(self):
        rows = self.wait.until(EC.visibility_of_all_elements_located(self.CLAIM_INFO))
        data_list = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'div.oxd-table-cell')
            row_data = [cell.text.strip() for cell in cells[:8]]
            data_list.append(row_data)
        return data_list

    @allure.step("Changes has been saved successfully")
    def is_search_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))

    @allure.step("Save claim information to CSV")
    def save_claim_info_to_csv(self, file_path):
        claim_info = self.get_claim_info()
        headers = ["Reference Id", "Employee Name", "Event Name", "Description", "Currency", "Submitted Date", "Status",
                   "Amount"]

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for row in claim_info:
                writer.writerow(row)
