import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import constants as utils
from pages.loginpage import LoginPage
from pages.productspage import Products
import pytest


class Test_TC001:

    global driver
    driver = webdriver.Chrome()

    @pytest.fixture  # Makes run everytime
    def test_setup(self):
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield  # After yield what to do after running the test
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("https://www.saucedemo.com/")

        lp = LoginPage(driver)
        lp.enter_username(utils.USERNAME)
        lp.enter_password(utils.PASSWORD)
        lp.click_login()
        page_name = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
        if page_name != "PRODUCTS":
            print(page_name)
            driver.save_screenshot("./screenshots/"+"login_test.png")
            assert False
