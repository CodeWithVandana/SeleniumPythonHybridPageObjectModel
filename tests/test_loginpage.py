import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from pages.HomePage import Homepage
from pages.Loginpage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

    @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel("E:/SeleniumPythonHybridFramework/ExcelFiles/TutorialsNinja.xlsx","TestLoginData"))
    def test_with_valid_credential(self,email_address,password):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credientials(email_address,password)
        time.sleep(3)
        login_page.verify_account_creation()

    def test_with_invalid_email_valid_password(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credientials(self.generate_email_with_timestamp(), "123456")
        time.sleep(5)
        expected_war = "Warning: No match for E-Mail Address and/or Password."
        #expected_war = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        assert login_page.get_no_product_message().__contains__(expected_war)

    def test_with_valid_email_invalid_password(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credientials("vandana1826@gmail.com", "123454556")
        expected_war = "Warning: No match for E-Mail Address and/or Password."
        #expected_war = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        assert login_page.get_no_product_message().__contains__(expected_war)

    def test_without_entering_credientials(self):
        home_page = Homepage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_with_credientials("", "")
        expected_war = "Warning: No match for E-Mail Address and/or Password."
        # expected_war = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
        assert login_page.get_no_product_message().__contains__(expected_war)















