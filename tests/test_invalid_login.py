import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from pages.loginpage import LoginPage
import pytest


class Test_TC002:

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
        lp.enter_username("TEST123")
        lp.enter_password("WORD")
        lp.click_login()

        wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[TimeoutException])
        error_msg = wait.until(EC.visibility_of_element_located((
            By.XPATH,  '//*[@id="login_button_container"]/div/form/div[3]/h3'
        )), message="Error message not found")
        assert error_msg.text == "Epic sadface: Username and password do not match any user in this service", "User logged in with invalid credentials"
