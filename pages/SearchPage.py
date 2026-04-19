from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_HP_product_link = "HP LP3065"
    no_product_message_xpath = "//*[@id='content']/p[2]"

    def display_status_of_product(self):
        return self.check_display_status_of_element("valid_HP_product_link",self.valid_HP_product_link)

    def retrive_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)

