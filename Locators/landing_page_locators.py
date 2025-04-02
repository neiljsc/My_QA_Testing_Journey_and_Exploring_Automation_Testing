from selenium.webdriver.common.by import By

class LandingPageLocators:

    """ Landing Page Data """
    landing_page_title = "JPetStore Demo"
    landing_page_header_text = "Welcome to JPetStore 6"
    landing_page_enter_store_link_button = "Enter the Store"
    landing_page_copyright_text = "Copyright www.mybatis.org"

    """ Landing Page Locators """
    landing_page_title_locator = (By.TAG_NAME, "title")
    landing_page_header_text_locator = (By.XPATH, "//h2[contains(text(),'Welcome to JPetStore 6')]")
    landing_page_enter_store_link_button_locator = (By.XPATH, "//a[contains(text(),'Enter the Store')]")
    landing_page_copyright_text_locator = (By.XPATH, "//div[@id='Content']//sub[contains(text(),'Copyright')]")