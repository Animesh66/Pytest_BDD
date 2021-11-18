#                                """Test Demo Web Shop feature tests."""

# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code

from pytest_bdd import scenarios, given, when, then, parsers

from tests.features.Page_Objects.Login_Page import LoginPage


@scenarios('..\\features\\demo_webshop.feature')
def test_login_functionality_of_demo_webshop():
    pass


@given('user opens the Demo Web Shop url')
def open_demo_web_shop_url(get_browser):
    get_browser.login = LoginPage(get_browser)
    get_browser.login.open_url()


@when(parsers.parse('user enter the {email} and {password}'))
def enter_email_password(get_browser, email, password):
    get_browser.login.enter_email_password(email, password)


@when('click on the LOG IN button')
def click_log_in_button(get_browser):
    get_browser.login.perform_login()


@then(parsers.parse('verify the page title is matching {home_page_title}'))
def verify_home_page_title(get_browser, home_page_title):
    get_browser.login.verify_homepage_title(home_page_title)
