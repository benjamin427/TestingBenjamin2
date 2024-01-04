from pages.AccountForm.AccountFormPage import CreateAccountPage
from utilities import excelfileReader
import pytest


@pytest.mark.usefixtures("setup_register_form")
class TestRegisterForm:

    @pytest.mark.parametrize("firstName, lastName, emailAddress, phoneNumber, companyName, streetAddress1, streetAddress2, city, state, postcode, whatsappMobile, password, passwordConfirm",
                            excelfileReader.get_excel_data("C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis_2/virtual_env/ExcelFiles/CreateAccountForm/PHP_Travels_CreateAccountForm_Fail.xlsx", "RandomEntry"))
    def test_complete_form(self, firstName, lastName, emailAddress, phoneNumber, companyName, streetAddress1, streetAddress2, city, state, postcode, whatsappMobile, password, passwordConfirm):
        enter_info = CreateAccountPage(self.driver)
        enter_info.enter_personal_information(firstName, lastName, emailAddress, phoneNumber)
        enter_info.enter_billing_info(companyName, streetAddress1, streetAddress2, city, state, postcode)
        enter_info.click_country_of_origin_united_states()
        enter_info.enter_whatsapp_number(whatsappMobile)
        enter_info.enter_password(password, passwordConfirm)
        enter_info.enter_whatsapp_number(whatsappMobile)
        enter_info.click_mailing_list_no()
        enter_info.click_register_button()