from selenium.webdriver.common.by import By
from .base_page import BasePage

class QualityAssurancePage(BasePage):
    QA_TEAM_LINK = (By.XPATH, "//h3[text()='Quality Assurance']")
    SEE_ALL_JOBS = (By.XPATH, "//a[text()='See all QA jobs']")

    def navigate_to_qa_team(self):
        self.click_element(*self.QA_TEAM_LINK)

    def navigate_to_jobs(self):
        self.click_element(*self.SEE_ALL_JOBS)
