from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class LoginForm:

    def __init__(self, driver):
        self.driver = driver

    login_email_address_text_field = "inputEmail"
    login_password_text_field = "inputPassword"
    login_button = "login"

    
    def enter_login_credentials(self, usernameEmail, password):
        self.driver.find_element(By.ID, self.login_email_address_text_field).send_keys(usernameEmail)
        self.driver.find_element(By.ID, self.login_password_text_field).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button).click()

