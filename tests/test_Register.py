import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from pages.HomePage import Homepage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class TestRegister(BaseTest):

    def test_register_with_mandatory_fields(self):
        email = self.generate_email_with_timestamp()
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_all_the_fields("vandana","mallaiah",email,"123456789","123456","123456","no","select")
        time.sleep(5)
        expected_message = "Your Account Has Been Created!"
        assert register_page.edit_account_created_message().__contains__(expected_message)

    def test_register_with_all_mandatory_fields(self):
        email = self.generate_email_with_timestamp()
        home_page = Homepage(self.driver)
        home_page.click_on_my_account()
        register_page = home_page.click_on_register_option()
        register_page.register_with_all_the_fields("vandana","mallaiah",email,"123456789","123456","123456","yes","select")
        time.sleep(5)
        expected_message = "Your Account Has Been Created!"
        assert register_page.edit_account_created_message().__contains__(expected_message)

    def test_register_with_duplicate_email(self):
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_all_the_fields("vandana","mallaiah","vandana1826@gmail.com","123456789","123456","123456","yes","select")
        time.sleep(5)
        expected_war = "Warning: E-Mail Address is already registered!"
        assert register_page.account_already_exists_warning_message().__contains__(expected_war)

    def test_register_without_entring_any_fields(self):
        home_page = Homepage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_with_all_the_fields("","","","","","","no","no")
        time.sleep(5)
        assert register_page.verify_warning_message(
                "Warning: You must agree to the Privacy Policy!",
                "First Name must be between 1 and 32 characters!",
                "Last Name must be between 1 and 32 characters!",
                "E-Mail Address does not appear to be valid!",
                "Telephone must be between 3 and 32 characters!",
                "Password must be between 4 and 20 characters!"
        )
