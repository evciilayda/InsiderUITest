import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class JobsPage(BasePage):
    LOCATION_FILTER = "filter-by-location"
    JOBS_LIST = (By.ID, "jobs-list")
    VIEW_ROLE = "(//a[text()='View Role'])[1]"

    def filter_jobs_by_location(self,location):
        self.scroll_by(400)
        time.sleep(10)
        select_element = self.driver.find_element(By.XPATH, "//select[@id='filter-by-location']")
        select = Select(select_element)
        select.select_by_visible_text(location)
        time.sleep(3)
        self.scroll_by(200)

    def verify_job_list_exists(self):
        return self.is_element_present(*self.JOBS_LIST)

    def verify_job_description(self):
        job_cards = self.driver.find_elements(By.CSS_SELECTOR, "div[class='position-list-item-wrapper bg-light']")
        self.scroll_by(200)
        for job in job_cards:
            try:

                position = job.find_element(By.XPATH, ".//p[@class='position-title font-weight-bold']").text
                department = job.find_element(By.CSS_SELECTOR,"span.position-department.text-large.font-weight-600.text-primary").text
                location = job.find_element(By.CSS_SELECTOR, "div.position-location.text-large").text

                print(f"Position: {position}, Department: {department}, Location: {location}")
            except Exception as e:
                print(f"An error occurred while extracting job details: {e}")

    def view_role(self):
        button =self.find_element(By.XPATH, self.VIEW_ROLE)
        action = ActionChains(self.driver)
        action.move_to_element(button).perform()
        button.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        new_tab_url = self.driver.current_url
        assert new_tab_url.startswith("https://jobs.lever.co/"), "Yanlış sayfaya yönlendirildiniz!"


