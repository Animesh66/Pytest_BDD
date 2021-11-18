import time

from tests.features.Page_Objects.Base_Page import BasePage
from tests.features.Page_Objects.Product_Review_Page import ProductReviewPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_catalog(self):
        time.sleep(3)
        self.click("catalog_XPATH")

    def navigate_product_review(self):
        self.click("product_review_XPATH")
        return ProductReviewPage(self.driver)
