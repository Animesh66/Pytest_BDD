from tests.features.Page_Objects.Base_Page import BasePage
from tests.features.Page_Objects.Home_Page import HomePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def enter_email_password(self, email, password):
        self.type("email_ID", email)
        self.type("password_ID", password)

    def perform_login(self):
        self.click("login_button_XPATH")
        return HomePage(self.driver)

    def verify_homepage_title(self, title):
        assert title in self.driver.title, "Actual page title does not match with expected page title"

