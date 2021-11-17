"""Test Demo Web Shop feature tests."""
# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code
from pytest_bdd import *


@scenario('features\demo_webshop.feature', 'Test Login functionality of Demo webshop')
def test_login_functionality_of_demo_webshop():
    pass

@given('user opens the Demo Web Shop url')
def user_opens_the_demo_web_shop_url():
    pass


@when('click on the LOG IN button')
def click_on_the_log_in_button():
    pass


@when('user enter the <email> and <password>')
def user_enter_the_email_and_password():
    pass


@then('user is able to successfully landed on the Home page')
def user_is_able_to_successfully_landed_on_the_home_page():
    pass


@then('verify the page title is matching <home_page_title>')
def verify_the_page_title_is_matching_home_page_title():
    pass
