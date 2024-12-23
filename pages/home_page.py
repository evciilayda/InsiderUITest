from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    COOKIE_POLICY = {'name': 'viewed_cookie_policy', 'value': 'no', 'domain': 'useinsider.com', 'path': '/', 'secure': True}
    COMPANY_LINK = (By.XPATH, "//a[contains(text(), 'Company')]")
    CAREERS_LINK = (By.XPATH, "//a[text()='Careers']")

    def accept_cookie(self):
        self.driver.add_cookie(self.COOKIE_POLICY)

    def navigate_to_company(self):
        self.click_element(*self.COMPANY_LINK)

    def navigate_to_careers(self):
        self.click_element(*self.CAREERS_LINK)
