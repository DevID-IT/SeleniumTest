import logging

from allure_commons.types import AttachmentType
from selenium.webdriver import Keys

from locators import locator
import allure

class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        # my account page elements
        self.username_input = locator.MyAccountPageLocators.username_input
        self.password_input = locator.MyAccountPageLocators.password_input
        self.reg_email_input = locator.MyAccountPageLocators.reg_email_input
        self.reg_password_input = locator.MyAccountPageLocators.reg_password_input
        self.logout_link = locator.MyAccountPageLocators.logout_link
        self.error_msg = locator.MyAccountPageLocators.error_msg
        self.register_name = locator.MyAccountPageLocators.register_name


    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.logger.info("Strona została otwarta")
        # self.driver.save_screenshot("C:\PycharmProjects\SeleniumTestSite\Screenshot\openpage.png")


    @allure.step("Otwarcie okna to '{1}' and '{2}'")
    def log_in(self, username, password):
        self.logger.info("Logujemy się do aplikacji za pomocą login: {username} i hasła: {password}".format(username=username, password=password))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        # self.driver.save_screenshot("C:\PycharmProjects\SeleniumTestSite\Screenshot\login.png")
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)
        allure.attach(self.driver.get_screenshot_as_png(), name="nazwa", attachment_type=AttachmentType.PNG)

    def create_account(self, email, password):
        self.logger.info("Tworzymy konto - email: {email}, hasło: {password}".format(email=email, password=password))
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.save_screenshot("C:\PycharmProjects\SeleniumTestSite\Screenshot\createaccount.png")
        self.driver.find_element(*self.register_name).click()

    def is_logout_link_displayed(self):
        self.logger.info("Sprawdzamy czy link jest widoczny")
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        self.logger.info("Sprawdzamy czy jest widoczny error")
        self.driver.save_screenshot("C:\PycharmProjects\SeleniumTestSite\Screenshot\errormsg.png")
        return self.driver.find_element(*self.error_msg).text

