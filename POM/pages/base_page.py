import time
from lib2to3.pgen2 import driver

from selenium.webdriver.chrome.webdriver import WebDriver
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, locator):
        time.sleep(0.8)
        self.driver.find_element(*locator).click()

    def fill_text(self, locator, txt: str) -> None:
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(txt)


    def get_text(self, locator) -> str:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except Exception as e:
            # Log the exception for debugging purposes
            return ""

    def get_url(self) -> str:
        time.sleep(1)
        return self.driver.current_url

    def from_list_click(self, i, locator):
        time.sleep(0.8)
        elements = self.driver.find_elements(*locator)
        if i < 0:
            print("Number of the item can't be negative")
        elif i >= len(elements):
            print(f"Index {i} is greater than the number of items in the list ({len(elements)})")
        else:
            elements[i].click()


    def return_price_from_list(self, i , locator):
        time.sleep(0.8)
        elements = self.driver.find_elements(*locator)
        if i < 0:
            print("Number of the item can't be negative")
        elif i >= len(elements):
            print(f"Index {i} is greater than the number of items in the list ({len(elements)})")
        else:
            price = self.get_text(elements[i])
            return price
