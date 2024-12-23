from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    TEAMS_BLOCK = "div[class='col-12 d-flex flex-wrap p-0 career-load-more']"
    LOCATIONS_BLOCK="div[class='col-12 d-flex flex-wrap']"
    LIFE_AT_INSIDER_BLOCK="div[class='elementor-widget-wrap elementor-element-populated e-swiper-container']"
    SEE_ALL_TEAMS =  "//a[text()='See all teams']"

    def careers_page_control(self):
        self.is_element_present(By.XPATH,self.TEAMS_BLOCK)
        self.is_element_present(By.XPATH,self.LOCATIONS_BLOCK)
        self.is_element_present(By.XPATH, self.LIFE_AT_INSIDER_BLOCK)


    def navigate_to_teams(self):
        self.find_element(By.XPATH,self.SEE_ALL_TEAMS)
        self.click_element(By.XPATH,self.SEE_ALL_TEAMS)
