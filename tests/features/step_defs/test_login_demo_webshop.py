#                                """Test Demo Web Shop feature tests."""

# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code
import pytest
from pytest_bdd import scenario, given, when, then, parsers


@scenario('features\demo_webshop.feature', 'Test Login functionality of Demo webshop')
def test_login_functionality_of_demo_webshop():
    pass


@given('user opens the Demo Web Shop url')
def open_demo_web_shop_url(get_browser):
    get_browser.get("https://admin-demo.nopcommerce.com/")


@when(parsers.parse('user enter the {email} and {password}'))
def enter_email_password(get_browser, email, password):
    get_browser.find_element_by_id("Email").send_keys(email)
    get_browser.find_element_by_id("Password").send_keys(password)


@when('click on the LOG IN button')
def click_log_in_button(get_browser):
    get_browser.find_element_by_xpath("//button[@type='submit']")


@then('user is able to successfully landed on the Home page')
@then(parsers.parse('verify the page title is matching {home_page_title}'))
def verify_home_page_title(get_browser, home_page_title):
    assert home_page_title in get_browser.title, "Page title does not match. Landed on incorrect page"
