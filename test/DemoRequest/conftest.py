from selenium import webdriver
from utilities.configurationReader import read_configuration
import pytest


@pytest.fixture
def setup_demo_request_form(request):
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
    url_demo_request_form = read_configuration("basic info", "url_php_travels_demopage")
    driver.get(url_demo_request_form)

    
