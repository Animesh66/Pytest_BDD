#                                """Test Demo Web Shop feature tests."""

# To generate code snippet use "pytest-bdd generate .\tests\features\demo_webshop.feature" code

from pytest_bdd import scenarios, given, when, then, parsers, scenario
from tests.features.Page_Objects.Home_Page import HomePage
from tests.features.Page_Objects.Login_Page import LoginPage
from tests.features.Page_Objects.Product_Review_Page import ProductReviewPage

# CONVERTERS = {
#     "email": str,
#     "password": str,
#     "home_page_title": str,
#     "product_review_page": str
# }


# @scenarios('..\\features\\demo_webshop.feature')

@scenario('..\\features\\demo_webshop.feature', 'Test Login functionality of Demo webshop')
def test_login_demo_webshop():
    pass


@scenario('..\\features\\demo_webshop.feature', 'Verify product review page')
def test_verify_product_review():
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


#                                    ****** Verify review page Scenario ******

@given('user click on Catalog menu')
def click_catalog_menu(get_browser):
    get_browser.home = HomePage(get_browser)
    get_browser.home.navigate_to_catalog()


@when('user click on Product Review submenu')
def click_product_review(get_browser):
    get_browser.home.navigate_product_review()


@then(parsers.parse('user navigated to {product_review_page} title'))
def verify_review_title(get_browser, product_review_page):
    get_browser.product_review = ProductReviewPage(get_browser)
    get_browser.product_review.verify_review_title(product_review_page)
