# what packages we want to import 
# how to define the test cases


from playwright.sync_api import Page, expect
import pytest
import sys

# def test_playwright_homepage(page:Page):
#     page.goto("https://playwright.dev/")

#    # page.pause()
#     expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
#     expect(page).to_have_url("https://playwright.dev/")
#     # wrapping the page in the assertion object
#     #assert page.title() == "Fast and reliable end-to-end testing for modern web apps | Playwright"


#     #class --- Page class
#     #interface --- expect


@pytest.mark.smoke(reason="This test is smoked for demonstration purposes")
@pytest.mark.regression(reason="This test is regressed for demonstration purposes")
def test_playwright_homepageNow1(page:Page):
    assert True


@pytest.mark.regression(reason="This test is expected to fail for demonstration purposes")
def test_playwright_homepageNow(page:Page):
    assert False

# @pytest.mark.fail(reason="This test is skipped for demonstration purposes")
# def test_playwright_homepageNow2(page:Page):
#     assert True
