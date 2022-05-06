from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select

class Products:

    def __init__(self, driver):
        self.driver = driver
        self.hamburger_menu_id = "react-burger-menu-btn"
        self.logout_link = "Logout"
        self.add_to_cart_btn = "add-to-cart-sauce-labs-backpack"
        self.select_filter_drop_down_xpath = '//*[@id="header_container"]/div[2]/div[2]/span/select'

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=10, ignored_exceptions=[TimeoutException])
        btn = wait.until(EC.element_to_be_clickable((By.ID, self.add_to_cart_btn)))
        btn.click()

    def filter_products_high_to_low(self):
        select = Select(self.driver.find_element(By.XPATH, self.select_filter_drop_down_xpath))
        select.select_by_visible_text('Price (high to low)')

    def click_hamburger_menu(self):
        self.driver.find_element(By.ID, self.hamburger_menu_id).click()

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        element.click()
