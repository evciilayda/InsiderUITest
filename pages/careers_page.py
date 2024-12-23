from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    SEE_ALL_TEAMS =  "//a[text()='See all teams']"

    def navigate_to_teams(self):
        self.find_element(By.XPATH,self.SEE_ALL_TEAMS)
        self.click_element(By.XPATH,self.SEE_ALL_TEAMS)
