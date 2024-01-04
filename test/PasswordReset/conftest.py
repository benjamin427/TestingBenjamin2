from selenium import webdriver
from utilities.configurationReader import read_configuration
import pytest


@pytest.fixture
def setup_password_reset_page(request):
    browser = read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        return "Choose browser to execute app"
    
    request.cls.driver = driver
    url_password_reset_page = read_configuration("basic info", "url_php_travels_passwordresetpage")
    driver.get(url_password_reset_page)

    