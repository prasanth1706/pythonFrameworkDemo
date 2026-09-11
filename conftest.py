 
import pytest
from playwright.sync_api import Page, expect

@pytest.fixture()
def test_login(page:Page):
            page.goto("https://google.com")
           # expect(page).to_have_url("https://www.google.com/") #( Assertion that checks if the current URL of the page matches the expected URL. It verifies that the navigation to the specified URL was successful. )
        #assert page.url == "https://www.google.com/" #( Test runner that interprets the test and executes it. It provides a way to run tests, collect results, and report failures. )
            return page

@pytest.fixture()
def testing(page:Page):
            page.goto("https://google.com")
           # expect(page).to_have_url("https://www.google.com/") #( Assertion that checks if the current URL of the page matches the expected URL. It verifies that the navigation to the specified URL was successful. )
        #assert page.url == "https://www.google.com/" #( Test runner that interprets the test and executes it. It provides a way to run tests, collect results, and report failures. )
            return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")


