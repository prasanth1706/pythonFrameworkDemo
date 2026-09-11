from time import time


class automationpracticeform:
    def __init__(self, page):
        self.page = page
        self.first_name_input = page.locator("#firstName")
        self.gender_radio_button = page.locator("#gender-radio-1")
        self.hobbies_checkbox = page.locator("#hobbies-checkbox-1")
        self.state_combobox = page.get_by_role("combobox").last
        self.city_combobox = page.get_by_role("combobox").nth(2)

    def fill_first_name(self, first_name):
        #time.sleep(20)  # Wait for 20 seconds to ensure the page is fully loaded
        self.first_name_input.wait_for(state="visible", timeout=20000)  # Wait for the first name input to be visible
        self.first_name_input.fill(first_name)

    def check_gender(self):
        self.gender_radio_button.check()

    def check_hobbies(self):
        self.hobbies_checkbox.check()

    def select_state(self, state):
        self.state_combobox.fill(state)
        self.page.get_by_text(state, exact=True).click()

    def select_city(self, city):
        self.city_combobox.fill(city)
        self.page.get_by_text(city, exact=True).click()