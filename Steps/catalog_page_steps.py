from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from behave import given, when, then
from Pages.catalog_page import CatalogPage
from Locators.catalog_page_locators import CatalogPageLocators
from Utilities.resource import CATALOG_URL

@given("user is on the catalog page")
def step_user_is_on_the_catalog_page(context):
    context.logger.info("Navigating to the catalog page.")
    context.driver.get(CATALOG_URL)
    context.catalog_page = CatalogPage(context.driver)
    context.catalog_page_locators = CatalogPageLocators()
    context.logger.info("Landed on the page: %s", CATALOG_URL)

@then('user should see the Catalog page title as "JPetStore Demo"')
def step_verify_page_title(context):
    context.logger.info("Verifying Catalog page title.")
    assert context.catalog_page.get_page_title() == CatalogPageLocators.catalog_page_title
    context.logger.info("Catalog page title verified: JPetStore Demo")

@then('user should see the following elements in the Header')
def step_verify_header_elements_visibility_and_text(context):
    context.logger.info("Checking visibility and text of header elements on the Catalog Page.")

    for row in context.table:
        element = row[0]

        if element == "JPetStore logo button":
            assert context.catalog_page.get_header_logo_button(), "Logo button is not visible"
        elif element == "Cart icon button":
            assert context.catalog_page.get_header_cart_icon(), "Cart icon is not visible"
        elif element == "Sign In link button":
            assert context.catalog_page.get_header_signin_link_button(), "Sign In link is not visible"
            actual_text = context.catalog_page.get_header_signin_link_button_text().strip()
            expected_text = "Sign In"
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Help link button":
            assert context.catalog_page.get_header_help_link_button(), "Help link is not visible"
            actual_text = context.catalog_page.get_header_help_link_button_text().strip()
            expected_text = "?"
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Search textbox":
            assert context.catalog_page.get_header_search_textbox(), "Search textbox is not visible"
        elif element == "Search button":
            assert context.catalog_page.get_header_search_button(), "Search button is not visible"
            actual_text = context.catalog_page.get_header_search_button_text().strip()
            expected_text = "Search"
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        else:
            assert False, f"Unknown element in table: {element}"

@then('user should see the following image buttons in the QuickLinks')
def step_verify_quicklinks_image_buttons(context):
    context.logger.info("Checking visibility of image buttons in the QuickLinks section.")

    for row in context.table:
        element = row[0]

        if element == "Fish image link button":
            assert context.catalog_page.get_quicklinks_fish_image_link_button(), "Fish image button is not visible"
        elif element == "Dogs image link button":
            assert context.catalog_page.get_quicklinks_dogs_image_link_button(), "Dogs image button is not visible"
        elif element == "Reptiles image link button":
            assert context.catalog_page.get_quicklinks_reptiles_image_link_button(), "Reptiles image button is not visible"
        elif element == "Cats image link button":
            assert context.catalog_page.get_quicklinks_cats_image_link_button(), "Cats image button is not visible"
        elif element == "Birds image link button":
            assert context.catalog_page.get_quicklinks_birds_image_link_button(), "Birds image button is not visible"
        else:
            assert False, f"Unknown element in table: {element}"

@then('user should see the following elements in the SidebarContent')
def step_verify_sidebar_content_icon_buttons_subtexts(context):
    context.logger.info("Checking visibility of icon buttons and subtexts in the SideBarContent section.")

    for row in context.table:
        element = row[0]

        if element == "Fish icon button":
            assert context.catalog_page.get_sidebar_content_fish_icon_button(), "Fish icon button is not visible"
            actual_text = context.catalog_page.get_sidebar_content_fish_subtext()
            expected_text = context.catalog_page_locators.catalog_page_fish_subtext
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Dogs icon button":
            assert context.catalog_page.get_sidebar_content_dogs_icon_button(), "Dogs icon button is not visible"
            actual_text = context.catalog_page.get_sidebar_content_dogs_subtext()
            expected_text = context.catalog_page_locators.catalog_page_dogs_subtext
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Cats icon button":
            assert context.catalog_page.get_sidebar_content_cats_icon_button(), "Cats icon button is not visible"
            actual_text = context.catalog_page.get_sidebar_content_cats_subtext()
            expected_text = context.catalog_page_locators.catalog_page_cats_subtext
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Reptiles icon button":
            assert context.catalog_page.get_sidebar_content_reptiles_icon_button(), "Reptiles icon button is not visible"
            actual_text = context.catalog_page.get_sidebar_content_reptiles_subtext()
            expected_text = context.catalog_page_locators.catalog_page_reptiles_subtext
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        elif element == "Birds icon button":
            assert context.catalog_page.get_sidebar_content_birds_icon_button(), "Birds icon button is not visible"
            actual_text = context.catalog_page.get_sidebar_content_birds_subtext()
            expected_text = context.catalog_page_locators.catalog_page_birds_subtext
            assert actual_text == expected_text, f"Expected text '{expected_text}' but got '{actual_text}'"
        else:
            assert False, f"Unknown element in table: {element}"