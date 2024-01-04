from selenium.webdriver.common.by import By

class PasswordResetField:

    def __init__(self, driver):
        self.driver = driver

    password_reset_text_field = "inputEmail"
    password_reset_submit_button = "//div/button[@class='btn btn-primary btn-recaptcha']"

    def enter_emailAddress(self, passwordReset):
        self.driver.find_element(By.ID, self.password_reset_text_field).send_keys(passwordReset)
    
    def click_submit_button(self):
        self.driver.find_element(By.XPATH, self.password_reset_submit_button).click()
    
