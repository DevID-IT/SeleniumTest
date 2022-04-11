import random

import pytest

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage


#zanim test się wykona zostanie utworzona (odpalona) metoda setup - czyli przeglądarka
@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:
    def test_update_billing_address(self):
        email = str(random.randint(1, 10000)) + "TesterOprogramowania@gmail.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, 'TesterOprogramowania')

        billing_address_page = BillingAddressPage(self.driver)
        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("Dan", "Trevloss")
        billing_address_page.set_company("None")
        billing_address_page.select_country("Poland")
        billing_address_page.set_address("Nowa 1", "01-001", "Warsaw")
        billing_address_page.set_phone_number("111-222-333")
        billing_address_page.save_address()

        assert "Address changed successfully" in billing_address_page.get_message_text()
