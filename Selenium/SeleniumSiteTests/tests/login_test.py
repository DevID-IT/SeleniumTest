import pytest
from pages.my_account_page import MyAccountPage
import allure

#zanim test się wykona zostanie utworzona (odpalona) metoda setup - czyli przeglądarka
@pytest.mark.usefixtures("setup")
class TestLogIn:
    @allure.title("To jest test dotyczący logowania pozytywnego")
    @allure.description("Opis jakiś do testu, Opis jakiś do testu Opis jakiś do testu Opis jakiś do testu")
    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in('TesterOprogramowania@gmail.com', 'TesterOprogramowania')
        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in('TesterOprogramowania@gmail.com', 'TesterOprogramowania-żle')
        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()
