from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.Loginpage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class Homepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    search_box_button_xpath = "//*[@id='search']/span/button"
    my_account_xpath = "//*[@id='top-links']/ul/li[2]/a"
    login_dropdown_xpath = "//*[@id='top-links']/ul/li[2]/ul/li[2]/a"
    register_option_xpath = "//*[@id='top-links']/ul/li[2]/ul/li[1]/a"

    def enter_product_into_searchbox_field(self, product_name):
        self.type_into_element(product_name,"search_box_field_name",self.search_box_field_name)

    def click_on_search_button(self):
        self.element_click("search_box_button_xpath",self.search_box_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account(self):
        self.element_click("my_account_xpath",self.my_account_xpath)

    def click_on_login_option(self):
        self.element_click("login_dropdown_xpath",self.login_dropdown_xpath)
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.element_click("register_option_xpath",self.register_option_xpath)
        return RegisterPage(self.driver)

    def search_for_a_product(self,productname):
        self.enter_product_into_searchbox_field(productname)
        return self.click_on_search_button()


    def navigate_to_login_page(self):
        self.click_on_my_account()
        return self.click_on_login_option()

    def navigate_to_register_page(self):
        self.click_on_my_account()
        return self.click_on_register_option()



