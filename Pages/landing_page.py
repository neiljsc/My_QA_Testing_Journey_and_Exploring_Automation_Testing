from Locators.landing_page_locators import LandingPageLocators

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def get_page_title(self):
        return self.driver.title

    def get_header_text(self):
        return self.driver.find_element(*LandingPageLocators.landing_page_header_text_locator).text

    def get_copyright_text(self):
        return self.driver.find_element(*LandingPageLocators.landing_page_copyright_text_locator).text

    def click_enter_store(self):
        self.driver.find_element(*LandingPageLocators.landing_page_enter_store_link_button_locator).click()