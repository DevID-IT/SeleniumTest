import logging

from selenium.webdriver.support.select import Select
from locators.locator import BillingAddressLocators


class BillingAddressPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # Billing Address Page elements
        self.addresses_link = BillingAddressLocators.addresses_link
        self.first_name_input = BillingAddressLocators.first_name_input
        self.last_name_input = BillingAddressLocators.last_name_input
        self.company_input = BillingAddressLocators.company_input
        self.country_select = BillingAddressLocators.country_select
        self.address_input = BillingAddressLocators.address_input
        self.postcode_input = BillingAddressLocators.postcode_input
        self.city_input = BillingAddressLocators.city_input
        self.phone_input = BillingAddressLocators.phone_input
        self.save_address_button = BillingAddressLocators.save_address_button
        self.msg_div = BillingAddressLocators.msg_div
        self.edit_link = BillingAddressLocators.edit_link

    def open_edit_billing_address(self):
        self.logger.info("Strona do edycji adresu faktury została otwarta")
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, first_name, last_name):
        self.logger.info("Zmieniamy dane personalne na imie: {firstname} i nazwisko: {lastname}".format(firstname=first_name, lastname=last_name))
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def select_country(self, country):
        self.logger.info("Zmieniamy dane kraju: {country}".format(country=country))
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city):
        self.logger.info("Zmieniamy dane adresowe - ulica: {street}, kod pocztowy: {postcode} i miasto: {city}".format(street=street, postcode=postcode, city=city))
        self.driver.find_element(*self.address_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone_number(self, phone_number):
        self.logger.info("Numer telefonu: {phonenumber}".format(phonenumber=phone_number))
        self.driver.find_element(*self.phone_input).send_keys(phone_number)

    def set_company(self, company):
        self.logger.info("Nazwa firmy: {company}".format(company=company))
        self.driver.find_element(*self.company_input).send_keys(company)

    def save_address(self):
        self.logger.info("Zapisujemy dane")
        self.driver.find_element(*self.save_address_button).click()

    def get_message_text(self):
        self.logger.info("Sprawdzam czy dostaliśmy wiadomość o sukcesie po zmianie")
        return self.driver.find_element(*self.msg_div).text

