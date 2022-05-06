import time

import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from pages.productspage import Products
from utils import constants as utils


class Test_TC004:

    global driver
    driver = webdriver.Chrome()

    @pytest.fixture
    def test_setup(self):
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("*** Filter Test Completed")

    def test_filter(self, test_setup):
        driver.get("https://www.saucedemo.com/")

        lp = LoginPage(driver)
        lp.enter_username(utils.USERNAME)
        lp.enter_password(utils.PASSWORD)
        lp.click_login()

        pp = Products(driver)
        pp.filter_products_high_to_low()
