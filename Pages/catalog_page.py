from Locators.catalog_page_locators import CatalogPageLocators

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver

    # Actions
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
        return self.driver.find_element(*CatalogPageLocators.catalog_page_signin_text).text

    def get_header_help_link_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_help_link_button_locator).is_displayed()
    def get_header_help_link_button_text(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_help_text).text

    def get_header_search_textbox(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_textbox_locator).is_displayed()

    def get_header_search_button(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_header_search_button_locator).is_displayed()
    def get_header_search_button_text(self):
        return self.driver.find_element(*CatalogPageLocators.catalog_page_search_text).text

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