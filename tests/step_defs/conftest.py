from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def get_browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
