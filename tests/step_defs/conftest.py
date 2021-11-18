from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.utils_config_reader import configuration_reader


@pytest.fixture()
def get_browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(configuration_reader("basic configuration", "test_url"))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
