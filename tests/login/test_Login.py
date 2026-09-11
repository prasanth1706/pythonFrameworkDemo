import time

import pytest
from playwright.sync_api import Page, expect
from pathlib import Path
import json

from pages.automation_practice_form import automationpracticeform

# Load test data from JSON file
with open(Path("testdata/registration_data.json")) as f:
    registration_data = json.load(f)

class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize("data", registration_data)
    def test_student_registration(self,page:Page, data):
        form_page = automationpracticeform(page)
        page.goto("https://demoqa.com/automation-practice-form")  #navigation, browser back button, forward button, refresh button, etc

        time.sleep(20)  # Wait for 20 seconds to ensure the page is fully loaded
        page.goto("https://demoqa.com/elements")  # Navigate to the elements page
        time.sleep(20)  # Wait for 20 seconds to ensure the page is fully loaded
        page.go_back()  # Navigate back to the previous page
       # time.sleep(20)  # Wait for 20 seconds to ensure the page is fully loaded
        page.wait_for_load_state("load")  # Wait for the page to fully load
        form_page.fill_first_name(data["first_name"])
        form_page.check_gender()
        form_page.check_hobbies()
        form_page.select_state(data["state"])
        form_page.select_city(data["city"])
        







            