from Locators.landing_page_locators import LandingPageLocators
from Utilities.helper import is_element_visible_and_clickable

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def get_page_title(self):
        return self.driver.title

    def get_header_text(self):
        header_element = self.driver.find_element(*LandingPageLocators.landing_page_header_text_locator)
        # Verify that the element is displayed
        if not header_element.is_displayed():
            raise Exception("Header text is not visible on the page.")
        # If it's displayed, return the text
        return header_element.text

    def get_copyright_text(self):
        footer_element = self.driver.find_element(*LandingPageLocators.landing_page_copyright_text_locator)
        # Verify that the element is displayed
        if not footer_element.is_displayed():
            raise Exception("Copyright text is not visible on the page.")
        # If it's displayed, return the text
        return footer_element.text

    def click_enter_store(self):
        try:
            # Check if the element is visible and clickable in one go
            enter_store_button = is_element_visible_and_clickable(self.driver,LandingPageLocators.landing_page_enter_store_link_button_locator)
            # Verify the button text
            button_text = enter_store_button.text.strip()
            if button_text != LandingPageLocators.landing_page_enter_store_link_button:
                raise Exception(
                    f"Button text is incorrect. Expected: '{LandingPageLocators.landing_page_enter_store_link_button}', but got: '{button_text}'")
            # Perform the click action
            enter_store_button.click()
        except Exception as e:
            raise Exception(f"Error while clicking 'Enter the Store' button: {str(e)}")