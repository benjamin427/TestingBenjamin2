from pages.DemoRequestForm.DemoRequestFormPage import DemoRequestForm
from utilities import excelfileReader
import pytest

@pytest.mark.usefixtures("setup_demo_request_form")
class TestDemoRequestForm:

    @pytest.mark.parametrize("firstName, lastName, businessName, emailAddress", excelfileReader.get_excel_data(
        "C:/Users/Benjamin Saint Elien/Documents/FrameworkAnalysis_2/virtual_env/ExcelFiles/DemoRequestForm/PHP_Travels_Demo_Request_Credentials_Fail.xlsx", "RandomInfo"
    ))
    def test_demo_request_form_entry(self, firstName, lastName, businessName, emailAddress):
        enter_credentials = DemoRequestForm(self.driver)
        enter_credentials.enter_info_credentials(firstName, lastName, businessName, emailAddress)
        enter_credentials.enter_result_number()
        enter_credentials.click_submit_button()



