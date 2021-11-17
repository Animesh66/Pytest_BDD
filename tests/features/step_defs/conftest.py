from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.utils_config_reader import configuration_reader


@pytest.fixture(params=["firefox", "chrome"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver
    driver.get(configuration_reader("basic configuration", "test_url"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
