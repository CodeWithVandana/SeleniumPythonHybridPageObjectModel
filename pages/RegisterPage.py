import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname_id = "input-firstname"
    lastname_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    subscribe_radio_xpath = "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input"
    policy_ckeckbox_name = "agree"
    continue_button_xpath = "//*[@id='content']/form/div/div/input[2]"
    edit_account_xpath = "//*[@id='content']/h1"
    account_already_exists_xpath = "//*[@id='account-register']/div[1]"
    policy_warning_xpath = "//*[@id='account-register']/div[1]"
    firstname_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    lastname_warning_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_message_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_message_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_message_xpath = "//input[@id='input-password']/following-sibling::div"

    #warnin messages
    expected_war_policy = "Warning: You must agree to the Privacy Policy!"
    expected_war_firstname = "First Name must be between 1 and 32 characters!"
    expected_war_lastname = "Last Name must be between 1 and 32 characters!"
    expected_war_email = "E-Mail Address does not appear to be valid!"
    expected_war_telephone = "Telephone must be between 3 and 32 characters!"
    expected_war_password = "Password must be between 4 and 20 characters!"

    def enter_firstname(self,firstname):
        self.type_into_element(firstname,"firstname_id",self.firstname_id)

    def enter_lastname(self,lastname):
        self.type_into_element(lastname,"lastname_id",self.lastname_id)

    def enter_email_aaddress(self,email):
        self.type_into_element(email,"email_id",self.email_id)

    def enter_telephone_number(self,telephone):
        self.type_into_element(telephone,"telephone_id",self.telephone_id)


    def enter_password(self,password):
        self.type_into_element(password,"password_id",self.password_id)

    def enter_confirm_password(self,confirm_password):
        self.type_into_element(confirm_password,"confirm_password_id",self.confirm_password_id)

    def click_on_subscribe_radio(self):
        self.element_click("subscribe_radio_xpath",self.subscribe_radio_xpath)

    def accept_policy_checkbox(self,):
        self.element_click("policy_ckeckbox_name",self.policy_ckeckbox_name)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)

    def edit_account_created_message(self):
        return self.retrieve_element_text("edit_account_xpath",self.edit_account_xpath)

    def account_already_exists_warning_message(self):
        return self.retrieve_element_text("account_already_exists_xpath",self.account_already_exists_xpath)

    def firstname_warning_message(self):
        return self.retrieve_element_text("firstname_warning_message_xpath",self.firstname_warning_message_xpath)

    def lastname_warning_message(self):
        return self.retrieve_element_text("lastname_warning_message_xpath",self.lastname_warning_message_xpath)

    def email_warning_message(self):
        return self.retrieve_element_text("email_warning_message_xpath",self.email_warning_message_xpath)

    def telephone_warning_message(self):
        return self.retrieve_element_text("telephone_warning_message_xpath",self.telephone_warning_message_xpath)

    def password_warning_message(self):
        return self.retrieve_element_text("password_warning_message_xpath",self.password_warning_message_xpath)

    def policy_warning_message(self):
        return self.retrieve_element_text("policy_warning_xpath",self.policy_warning_xpath)


    def register_with_all_the_fields(self,firstname,lastname,email,telephone,password,confirm_password,yes_or_no,policy):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email_aaddress(email)
        self.enter_telephone_number(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        if yes_or_no.__eq__("yes"):
            self.click_on_subscribe_radio()
        if policy.__eq__("select"):
            self.accept_policy_checkbox()
        return self.click_on_continue_button()


    def verify_warning_message(self,expected_war_policy,expected_war_firstname,expected_war_lastname,expected_war_email,expected_war_telephone,expected_war_password):
        actual_expected_war_policy = self.policy_warning_message()
        actual_expected_war_firstname = self.firstname_warning_message()
        actual_expected_war_lastname = self.lastname_warning_message()
        actual_expected_war_email = self.email_warning_message()
        actual_expected_war_telephone = self.telephone_warning_message()
        actual_expected_war_password = self.password_warning_message()

        status = False

        if expected_war_policy.__eq__(actual_expected_war_policy):
            if expected_war_firstname.__eq__(actual_expected_war_firstname):
                if expected_war_lastname.__eq__(actual_expected_war_lastname):
                    if expected_war_email.__eq__(actual_expected_war_email):
                        if expected_war_telephone.__eq__(actual_expected_war_telephone):
                            if expected_war_password.__eq__(actual_expected_war_password):
                                status = True

        return status





