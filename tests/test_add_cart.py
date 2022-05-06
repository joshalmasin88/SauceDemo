import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from pages.loginpage import LoginPage
from pages.productspage import Products
from utils import constants as utils
import pytest


class Test_TC003:

    global driver
    driver = webdriver.Chrome()

    @pytest.fixture
    def test_setup(self):
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield  # After yield what to do after running the test
        driver.close()
        driver.quit()
        print("*** Add To Cart Test Completed")

    def test_cart(self, test_setup):
        driver.get("https://www.saucedemo.com/")

        lp = LoginPage(driver)
        lp.enter_username(utils.USERNAME)
        lp.enter_password(utils.PASSWORD)
        lp.click_login()

        pp = Products(driver)
        pp.add_to_cart()
        wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[TimeoutException])
        cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge')))
        assert cart_icon.text is "1"