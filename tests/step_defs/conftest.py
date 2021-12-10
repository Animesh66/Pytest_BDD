from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(params=["chrome", "firefox"])
# def get_browser(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     if request.param == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     request.driver = driver
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

@pytest.fixture()
def get_browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()