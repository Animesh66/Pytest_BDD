"""Test Demo Web Shop feature tests."""
# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code

from pytest_bdd import scenario, given, when, then, parsers


@scenario('features\demo_webshop.feature', 'Test Login functionality of Demo webshop')
def test_login_functionality_of_demo_webshop():
    pass


@given('user opens the Demo Web Shop url')
def open_demo_web_shop_url(get_browser):
    pass


@when('click on the LOG IN button')
def click_log_in_button(get_browser):
    pass


@when(parsers.parse('user enter the <email> and <password>'))
def enter_email_password(get_browser):
    pass


@then('user is able to successfully landed on the Home page')
def landed_on_the_home_page(get_browser):
    pass


@then('verify the page title is matching <home_page_title>')
def verify_home_page_title(get_browser):
    pass
