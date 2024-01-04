from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC 



class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver

    personal_information_first_name = "firstname"
    personal_information_last_name = "lastname"
    personal_information_email = "email"
    personal_information_phone = "phonenumber"

    billing_address_company_name = "companyname"
    billing_address_street_address = "address1"
    billing_address_street_address_2 = "address2"
    billing_address_city = "city"
    billing_address_state = "state"
    billing_address_postcode = "postcode"
    billing_address_countrySelect = "inputCountry"

    additional_info_required_whatsapp = "customfield[2]"

    account_security_password = "password"
    account_security_passwordConfirmed = "password2"

    mailing_list_option_yes = "//div/span[@class='bootstrap-switch-handle-on bootstrap-switch-success']"
    mailing_list_option_no = "//div/span[@class='bootstrap-switch-label']"

    recaptcha_checkbox = "recaptcha-checkbox-border"

    register_button = "//p/input[@class='btn btn-large btn-primary btn-recaptcha']"

    def enter_personal_information(self, firstName, lastName, emailAddress, phoneNumber):
        self.driver.find_element(By.NAME, self.personal_information_first_name).send_keys(firstName)
        self.driver.find_element(By.NAME, self.personal_information_last_name).send_keys(lastName)
        self.driver.find_element(By.NAME, self.personal_information_email).send_keys(emailAddress)
        self.driver.find_element(By.NAME, self.personal_information_phone).send_keys(phoneNumber)

    def enter_billing_info(self, companyName, streetAddres1, streetAddress2, city, state, postcode):
        self.driver.find_element(By.NAME, self.billing_address_company_name).send_keys(companyName)
        self.driver.find_element(By.NAME, self.billing_address_street_address).send_keys(streetAddres1)
        self.driver.find_element(By.NAME, self.billing_address_street_address_2).send_keys(streetAddress2)
        self.driver.find_element(By.NAME, self.billing_address_city).send_keys(city)
        self.driver.find_element(By.NAME, self.billing_address_state).send_keys(state)
        self.driver.find_element(By.NAME, self.billing_address_postcode).send_keys(postcode)

    def click_country_of_origin_united_states(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("United States")
    
    def click_country_of_origin_canada(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("Canada")

    def click_country_of_origin_united_kingdom(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("United Kingdom")

    def click_country_of_origin_brazil(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("Brazil")

    def click_country_of_origin_germany(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("Germany")

    def click_country_of_origin_australia(self):
        select_country = Select(self.driver.find_element(By.ID, self.billing_address_countrySelect))
        select_country.select_by_visible_text("Australia")

    def enter_whatsapp_number(self, whatsAppPhoneNumber):
        self.driver.find_element(By.NAME, self.additional_info_required_whatsapp).send_keys(whatsAppPhoneNumber)

    def enter_password(self, password, passwordConfirmed):
        self.driver.find_element(By.NAME, self.account_security_password).send_keys(password)
        self.driver.find_element(By.NAME, self.account_security_passwordConfirmed).send_keys(passwordConfirmed)
    
    def click_mailing_list_no(self):
        cursor_action = ActionChains(self.driver)
        move = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mailing_list_option_no))
        )
        cursor_action.move_to_element(move).click().perform()

    def click_mailing_list_yes(self):
        cursor_action = ActionChains(self.driver)
        move = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.mailing_list_option_yes))
        )
        cursor_action.move_to_element(move).click().perform()

    def click_register_button(self):
        cursor_action = ActionChains(self.driver)
        move = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.register_button))
        )
        cursor_action.move_to_element(move).click().perform()

        
    


