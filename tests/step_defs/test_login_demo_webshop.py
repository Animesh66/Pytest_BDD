#                                """Test Demo Web Shop feature tests."""

# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code


import pytest
from pytest_bdd import scenario, given, when, then, parsers

from tests.features.Page_Objects.Login_Page import LoginPage


@scenario('..\\features\\demo_webshop.feature', 'Test Login functionality of Demo webshop')
def test_login_functionality_of_demo_webshop():
    pass


@pytest.mark.usefixtures("get_browser")
@given('user opens the Demo Web Shop url')
def open_demo_web_shop_url(context):
    login = LoginPage(context.driver)
    login.open_url()


@pytest.mark.usefixtures("get_browser")
@when(parsers.parse('user enter the {email} and {password}'))
def enter_email_password(context, email, password):
    context.login.enter_email_password(email, password)


@pytest.mark.usefixtures("get_browser")
@when('click on the LOG IN button')
def click_log_in_button(context):
    context.login.perform_login()


@pytest.mark.usefixtures("get_browser")
@then(parsers.parse('verify the page title is matching {home_page_title}'))
def verify_home_page_title(context, home_page_title):
    context.login.verify_title(home_page_title)
