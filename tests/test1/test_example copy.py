# what packages we want to import 
# how to define the test cases
import pytest

from playwright.sync_api import Page

@pytest.mark.readonly
def test_playwright_homepage(page:Page):
    page.goto("https://demoqa.com/automation-practice-form")
  
    page.get_by_role("textbox", name="First Name").fill("Jane")
    
    page.get_by_role("textbox", name="Last Name").fill("Willams")

    page.locator("div").filter(has_text=re.compile(r"^Male$")).click()
   
    page.get_by_role("textbox", name="Mobile Number").fill("9988552244")