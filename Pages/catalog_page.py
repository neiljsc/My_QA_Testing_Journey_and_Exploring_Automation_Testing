from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Locators.catalog_page_locators import CatalogPageLocators

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver

    #Web title
    def get_page_title(self):
        return self.driver.title
    #SideBarContent Descriptions
    def is_text_visible_in_sidebar(self, expected_text):
        try:
            sidebar = self.driver.find_element(*CatalogPageLocators.SIDEBAR_CONTENT)
            return expected_text in sidebar.text
        except (NoSuchElementException, StaleElementReferenceException):
            return False
    #Separator CTA Message
    def is_cta_message_visible_in_separator(self, expected_text):
        try:
            separator = self.driver.find_element(*CatalogPageLocators.SEPARATOR_CTA_MESSAGE)
            return expected_text in separator.text
        except (NoSuchElementException, StaleElementReferenceException):
            return False
    #Footer texts
    def are_texts_visible_in_footer(self, expected_text):
        try:
            footer = self.driver.find_element(*CatalogPageLocators.FOOTER_TEXTS)
            return expected_text in footer.text
        except (NoSuchElementException, StaleElementReferenceException):
            return False

    #Header - Verify page redirections
    def click_header_logo_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_header_logo_button_locator)).click()
    def click_header_cart_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_header_cart_icon_button_locator)).click()
    def click_header_signin_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_header_sign_in_link_button_locator)).click()
    def click_header_help_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_header_help_link_button_locator)).click()

    #QuickLinks - Verify page redirections
    def click_quicklinks_fish_image_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_fish_image_link_button_locator)).click()
    def click_quicklinks_dogs_image_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_dogs_image_link_button_locator)).click()
    def click_quicklinks_reptiles_image_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_reptiles_image_link_button_locator)).click()
    def click_quicklinks_cats_image_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_cats_image_link_button_locator)).click()
    def click_quicklinks_birds_image_link_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_birds_image_link_button_locator)).click()

    #SideBarContent - Verify page redirections
    def click_sidebar_content_fish_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_fish_icon_button_locator)).click()
    def click_sidebar_content_dogs_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_dogs_icon_button_locator)).click()
    def click_sidebar_content_reptiles_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_reptiles_icon_button_locator)).click()
    def click_sidebar_content_cats_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_cats_icon_button_locator)).click()
    def click_sidebar_content_birds_icon_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(CatalogPageLocators.catalog_page_birds_icon_button_locator)).click()

    #def get_header_search_textbox(self):
    #    return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_textbox_locator).is_displayed()
    #def get_header_search_button(self):
    #    return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_button_locator).is_displayed()
    #def get_header_search_button_text(self):
    #    return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_button_locator).get_attribute('value')