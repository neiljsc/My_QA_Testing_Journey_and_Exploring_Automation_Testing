from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from behave import given, when, then
from Pages.landing_page import LandingPage
from Locators.landing_page_locators import LandingPageLocators
from Utilities.resource import LANDING_URL

@given("user is on the landing page")
def step_user_is_on_the_landing_page(context):
    context.logger.info("Navigating to the landing page.")
    context.driver.get(LANDING_URL)
    context.landing_page = LandingPage(context.driver)
    context.logger.info("Landed on the page: %s", LANDING_URL)

@then('user should see the Landing page title as "JPetStore Demo"')
def step_verify_page_title(context):
    context.logger.info("Verifying Landing page title.")
    assert context.landing_page.get_page_title() == LandingPageLocators.landing_page_title
    context.logger.info("Landing page title verified: JPetStore Demo")

@then('user should see the header text')
def step_verify_header_text(context):
    context.logger.info("Verifying header text.")
    assert context.landing_page.get_header_text() == LandingPageLocators.landing_page_header_text
    context.logger.info("Header text verified: Welcome to JPetStore 6")

@then('user should see the link button')
def step_verify_enter_store_button(context):
    context.logger.info('Verifying link button "Enter the Store".')
    button = context.driver.find_element(*LandingPageLocators.landing_page_enter_store_link_button_locator)
    assert button.is_displayed() and button.text.strip() == LandingPageLocators.landing_page_enter_store_link_button
    context.logger.info('Link button "Enter the Store" is visible and has correct text.')

@then('user should see the copyright text')
def step_verify_copyright_text(context):
    context.logger.info('Verifying copyright text.')
    assert context.landing_page.get_copyright_text() == LandingPageLocators.landing_page_copyright_text
    context.logger.info('Copyright text verified: Copyright www.mybatis.org')

@when('user clicks on link button')
def step_click_enter_store(context):
    context.logger.info('Clicking on "Enter the Store" link.')
    context.landing_page.click_enter_store()
    context.logger.info('Clicked on "Enter the Store" link.')

@then('user should be redirected to the Catalog Page with URL "https://petstore.octoperf.com/actions/Catalog.action"')
def step_verify_redirected_url(context):
    context.logger.info('Verifying redirection to Catalog page.')
    try:
        WebDriverWait(context.driver, 10).until(
            ec.url_to_be("https://petstore.octoperf.com/actions/Catalog.action"))
        context.logger.info('Redirected to Catalog page successfully.')
    except TimeoutException:
        context.logger.error(f"Expected URL not found. Current URL: {context.driver.current_url}")
        raise Exception("Timeout waiting for the Catalog page URL.")