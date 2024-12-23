import time

import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qualityassurance_page import QualityAssurancePage
from pages.jobs_page import JobsPage

def test_insider(driver):
    home_page = HomePage(driver)
    careers_page = CareersPage(driver)
    qa_page = QualityAssurancePage(driver)
    jobs_page = JobsPage(driver)
    home_page.accept_cookie()
    home_page.navigate_to_company()
    home_page.navigate_to_careers()
    careers_page.navigate_to_teams()
    qa_page.navigate_to_qa_team()
    qa_page.navigate_to_jobs()
    jobs_page.filter_jobs_by_location("Istanhbul, Turkey")
    assert jobs_page.verify_job_list_exists(), "Job list bulunamadı!"
    jobs_page.view_role()
