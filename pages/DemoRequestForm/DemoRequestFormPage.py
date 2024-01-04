from selenium.webdriver.common.by import By

class DemoRequestForm:

    def __init__(self, driver):
        self.driver = driver

    instantDemoRequestForm_firstName_text_field = "first_name"
    instantDemoRequestForm_lastName_text_field = "last_name"
    instantDemoRequestForm_businessName_text_field = "business_name"
    instantDemoRequestForm_email_text_field = "email"

    instantDemoRequestForm_result_text_field = "number"
    instantDemoRequestForm_submitButton = "demo"

    def enter_info_credentials(self, firstName, lastName, businessName, emailAddress):
        self.driver.find_element(By.NAME, self.instantDemoRequestForm_firstName_text_field).send_keys(firstName)
        self.driver.find_element(By.NAME, self.instantDemoRequestForm_lastName_text_field).send_keys(lastName)
        self.driver.find_element(By.NAME, self.instantDemoRequestForm_businessName_text_field).send_keys(businessName)
        self.driver.find_element(By.NAME, self.instantDemoRequestForm_email_text_field).send_keys(emailAddress)

    def enter_result_number(self):
        self.driver.find_element(By.ID, self.instantDemoRequestForm_result_text_field).send_keys("5") 
        self.driver.find_element(By.ID, self.instantDemoRequestForm_submitButton).click()
    
    def click_submit_button(self):
        self.driver.find_element(By.ID, self.instantDemoRequestForm_submitButton).click()
    