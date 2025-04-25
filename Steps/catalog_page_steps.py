from time import sleep

from behave import given, when, then
from Pages.catalog_page import CatalogPage
from Locators.catalog_page_locators import CatalogPageLocators
from Utilities.resource import CATALOG_URL, SIGNIN_URL, HELP_URL, CART_URL, FISH_PAGE_URL, DOGS_PAGE_URL, \
    REPTILES_PAGE_URL, CATS_PAGE_URL, BIRDS_PAGE_URL


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

@then('user should see the correct subtexts in the SidebarContent')
def step_verify_sidebar_content_icon_buttons_subtexts(context):
    context.logger.info("Checking visibility of subtexts in the SideBarContent section.")
    for row in context.table:
        expected_subtext = row[0]
        # Check subtext visibility
        is_subtext_visible = context.catalog_page.is_text_visible_in_sidebar(expected_subtext)
        assert is_subtext_visible, f"Subtext '{expected_subtext}'"

@then('user should see the correct CTA message in the Separator')
def step_verify_separator_cta_message(context):
    context.logger.info("Checking visibility of CTA message in the Separator section.")
    for row in context.table:
        expected_subtext = row[0]
        # Check CTA message visibility
        is_separator_cta_message_visible = context.catalog_page.is_cta_message_visible_in_separator(expected_subtext)
        assert is_separator_cta_message_visible, f"Subtext '{expected_subtext}'"

@then('user should see the correct texts in the Footer')
def step_verify_footer_texts(context):
    context.logger.info("Checking visibility of texts in the Footer section.")
    for row in context.table:
        expected_subtext = row[0]
        # Check Footer texts visibility
        are_footer_texts_visible = context.catalog_page.are_texts_visible_in_footer(expected_subtext)
        assert are_footer_texts_visible, f"Subtext '{expected_subtext}'"

# Header - Verify page redirections
@when('user clicks the JPetStore logo button')
def step_click_jpetstore_logo_button(context):
    context.logger.info("Clicking the JPetStore logo button..")
    context.catalog_page.click_header_logo_button()
@then('page should refresh and display the Catalog Page with URL "{expected_url}"')
def step_verify_catalog_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"

@when('user clicks the Cart icon button')
def step_click_cart_icon_button(context):
    context.logger.info("Clicking the Cart icon button..")
    context.catalog_page.click_header_cart_icon_button()
@then('user should be redirected to the Cart Page with URL "{expected_url}"')
def step_verify_cart_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", CART_URL)

@when('user clicks the Sign In link button')
def step_click_signin_link_button(context):
    context.logger.info("Clicking the Sign In link button..")
    context.catalog_page.click_header_signin_link_button()
@then('user should be redirected to the Sign In Page with URL "{expected_url}"')
def step_verify_signin_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", SIGNIN_URL)

@when('user clicks the Help link button')
def step_click_help_link_button(context):
    context.logger.info("Clicking the Help link button..")
    context.catalog_page.click_header_help_link_button()
@then('user should be redirected to the Help Page with URL "{expected_url}"')
def step_verify_help_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", HELP_URL)

# Quicklinks - Verify page redirections
@when('user clicks the Fish image button in the QuickLinks')
def step_click_fish_image_button(context):
    context.logger.info("Clicking the Fish image button in the Quicklinks..")
    context.catalog_page.click_quicklinks_fish_image_link_button()
@then('user should be redirected to the Fish Category Page with URL "{expected_url}"')
def step_verify_fish_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", FISH_PAGE_URL)
@when('user clicks the Dogs image button in the QuickLinks')
def step_click_dogs_image_button(context):
    context.logger.info("Clicking the Dogs image button in the Quicklinks..")
    context.catalog_page.click_quicklinks_dogs_image_link_button()
@then('user should be redirected to the Dogs Category Page with URL "{expected_url}"')
def step_verify_dogs_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", DOGS_PAGE_URL)
@when('user clicks the Reptiles image button in the QuickLinks')
def step_click_reptiles_image_button(context):
    context.logger.info("Clicking the Reptiles image button in the Quicklinks..")
    context.catalog_page.click_quicklinks_reptiles_image_link_button()
@then('user should be redirected to the Reptiles Category Page with URL "{expected_url}"')
def step_verify_reptiles_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", REPTILES_PAGE_URL)
@when('user clicks the Cats image button in the QuickLinks')
def step_click_cats_image_button(context):
    context.logger.info("Clicking the Cats image button in the Quicklinks..")
    context.catalog_page.click_quicklinks_cats_image_link_button()
@then('user should be redirected to the Cats Category Page with URL "{expected_url}"')
def step_verify_cats_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", CATS_PAGE_URL)
@when('user clicks the Birds image button in the QuickLinks')
def step_click_birds_image_button(context):
    context.logger.info("Clicking the Birds image button in the Quicklinks..")
    context.catalog_page.click_quicklinks_birds_image_link_button()
@then('user should be redirected to the Birds Category Page with URL "{expected_url}"')
def step_verify_birds_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", BIRDS_PAGE_URL)

# SideBarContent - Verify page redirections
@when('user clicks the Fish icon button in the SidebarContent')
def step_click_fish_icon_button(context):
    context.logger.info("Clicking the Fish icon button in the SideBarContent..")
    context.catalog_page.click_sidebar_content_fish_icon_button()
@then('Fish Category Page should be displayed with URL "{expected_url}"')
def step_verify_fish_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", FISH_PAGE_URL)
@when('user clicks the Dogs icon button in the SidebarContent')
def step_click_dogs_icon_button(context):
    context.logger.info("Clicking the Dogs icon button in the SideBarContent..")
    context.catalog_page.click_sidebar_content_dogs_icon_button()
@then('Dogs Category Page should be displayed with URL "{expected_url}"')
def step_verify_dogs_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", DOGS_PAGE_URL)
@when('user clicks the Reptiles icon button in the SidebarContent')
def step_click_reptiles_icon_button(context):
    context.logger.info("Clicking the Reptiles icon button in the SideBarContent..")
    context.catalog_page.click_sidebar_content_reptiles_icon_button()
@then('Reptiles Category Page should be displayed with URL "{expected_url}"')
def step_verify_reptiles_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", REPTILES_PAGE_URL)
@when('user clicks the Cats icon button in the SidebarContent')
def step_click_cats_icon_button(context):
    context.logger.info("Clicking the Cats icon button in the SideBarContent..")
    context.catalog_page.click_sidebar_content_cats_icon_button()
@then('Cats Category Page should be displayed with URL "{expected_url}"')
def step_verify_cats_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", CATS_PAGE_URL)
@when('user clicks the Birds icon button in the SidebarContent')
def step_click_birds_icon_button(context):
    context.logger.info("Clicking the Birds icon button in the SideBarContent..")
    context.catalog_page.click_sidebar_content_birds_icon_button()
@then('Birds Category Page should be displayed with URL "{expected_url}"')
def step_verify_birds_page_redirection(context, expected_url):
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL '{expected_url}', but got '{actual_url}'"
    context.logger.info("Landed on the page: %s", BIRDS_PAGE_URL)
