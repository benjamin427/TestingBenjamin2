from pages.PasswordReset.PasswordResetPage import PasswordResetField
from utilities import excelfileReader
import pytest


@pytest.mark.usefixtures("setup_password_reset_page")
class TestPasswordReset:

    @pytest.mark.parametrize("emailAddress", 
                             excelfileReader.get_excel_data("C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis_2/virtual_env/ExcelFiles/PasswordReset/PHP_Travels_PasswordReset_Fail.xlsx", "RandomInfo"))
    
    def test_password_reset_page(self, emailAddress):
        enter_email = PasswordResetField(self.driver)
        enter_email.enter_emailAddress(emailAddress)

        click = PasswordResetField(self.driver)
        click.click_submit_button()
