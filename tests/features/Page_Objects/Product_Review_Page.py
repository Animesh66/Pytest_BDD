from tests.features.Page_Objects.Base_Page import BasePage


class ProductReviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_reviews_input(self, created_from_date, created_to_date):
        self.click("created_from_date_XPATH")
        self.type("created_from_date_XPATH", created_from_date)
        self.click("created_to_date_XPATH")
        self.type("created_to_date_XPATH", created_to_date)
        self.click("search_button_XPATH")

    def verify_review_title(self, title):
        assert title in self.driver.title, "Actual page title does not match with expected page title"
