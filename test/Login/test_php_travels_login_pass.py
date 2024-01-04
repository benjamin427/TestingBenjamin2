from pages.Login.LoginForm import LoginForm
from utilities import excelfileReader
import pytest


@pytest.mark.usefixtures("setup_login_form")
class TestLoginForm:

    @pytest.mark.parametrize("usernameEmail, password", 
                             excelfileReader.get_excel_data("C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis_2/virtual_env/ExcelFiles/Login/PHP_Travels_LoginForm_Pass.xlsx", "LoginCredentials"))
    
    def test_login_form(self, usernameEmail, password):
        enter_credentials = LoginForm(self.driver)
        enter_credentials.enter_login_credentials(usernameEmail, password)
        enter_credentials.click_login_button()
    
    