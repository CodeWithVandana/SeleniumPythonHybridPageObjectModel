import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.HomePage import Homepage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_for_a_vaild_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        time.sleep(3)
        assert search_page.valid_HP_product_link

    def test_search_for_a_invalid_product(self):
        home_page = Homepage(self.driver)
        search_page = home_page.search_for_a_product("Honda")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_message().__eq__(expected_text)

    def test_search_without_product(self):
        home_page = Homepage(self.driver)
        home_page.enter_product_into_searchbox_field("")
        search_page = home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrive_no_product_message.__eq__(expected_text)


