from selenium.webdriver.support.wait import WebDriverWait
from Locators.catalog_page_locators import CatalogPageLocators
from selenium.webdriver.support import expected_conditions as ec

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver

    #Web title
    def get_page_title(self):
        return self.driver.title

    #Header
    def get_header_logo_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_logo_button_locator).is_displayed()
    def get_header_cart_icon(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_cart_icon_button_locator).is_displayed()
    def get_header_signin_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_sign_in_link_button_locator).is_displayed()
    def get_header_signin_link_button_text(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_sign_in_link_button_locator).text
    def get_header_help_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_help_link_button_locator).is_displayed()
    def get_header_help_link_button_text(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_help_link_button_locator).text
    def get_header_search_textbox(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_textbox_locator).is_displayed()
    def get_header_search_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_button_locator).is_displayed()
    def get_header_search_button_text(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_button_locator).get_attribute('value')

    #QuickLinks
    def get_quicklinks_fish_image_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_fish_image_link_button_locator).is_displayed()
    def get_quicklinks_dogs_image_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_dogs_image_link_button_locator).is_displayed()
    def get_quicklinks_reptiles_image_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_reptiles_image_link_button_locator).is_displayed()
    def get_quicklinks_cats_image_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_cats_image_link_button_locator).is_displayed()
    def get_quicklinks_birds_image_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_birds_image_link_button_locator).is_displayed()

    #SideBarContent
    def get_sidebar_content_fish_icon_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_fish_icon_button_locator).is_displayed()
    def get_sidebar_content_fish_subtext(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_fish_subtext_locator).text
    def get_sidebar_content_dogs_icon_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_dogs_icon_button_locator).is_displayed()
    def get_sidebar_content_dogs_subtext(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_dogs_subtext_locator).text
    def get_sidebar_content_cats_icon_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_cats_icon_button_locator).is_displayed()
    def get_sidebar_content_cats_subtext(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_cats_subtext_locator).text
    def get_sidebar_content_reptiles_icon_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_reptiles_icon_button_locator).is_displayed()
    def get_sidebar_content_reptiles_subtext(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_reptiles_subtext_locator).text
    def get_sidebar_content_birds_icon_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_birds_icon_button_locator).is_displayed()
    def get_sidebar_content_birds_subtext(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_birds_subtext_locator).text