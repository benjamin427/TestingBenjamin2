from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.configurationReader import read_configuration
import pytest


@pytest.fixture
def setup_register_form(request):
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
    url_create_account_form = read_configuration("basic info", "url_php_travels_createaccountpage")
    driver.get(url_create_account_form)

    
    

   


    
