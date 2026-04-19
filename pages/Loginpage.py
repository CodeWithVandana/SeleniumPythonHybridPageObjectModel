from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_xpath = "//*[@id='input-email']"
    password_id = "input-password"
    login_button_xpath = "//*[@id='content']/div/div[2]/div/form/input"
    account_created_link = "Edit your account information"
    no_product_message_xpath = "//*[@id='account-login']/div[1]"

    def enter_email_address(self,email_text):
        self.type_into_element(email_text,"email_xpath",self.email_xpath)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_id",self.password_id)

    def click_on_login_button(self):
        self.element_click("login_button_xpath",self.login_button_xpath)
        return LoginPage(self.driver)

    def verify_account_creation(self):
        return self.check_display_status_of_element("account_created_link",self.account_created_link)

    def get_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)

    def login_with_credientials(self,email_text,password_text):
        self.enter_email_address(email_text)
        self.enter_password(password_text)
        return self.click_on_login_button()
