import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_to_cart_btn(self):
        push = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        push.click()
    def same_title(self):
        print(self.browser.find_element(*ProductPageLocators.TITLE_NAME).text)
        print(self.browser.find_element(*ProductPageLocators.CART_TITLE_NAME).text)
        assert self.browser.find_element(*ProductPageLocators.TITLE_NAME).text in self.browser.find_element(
            *ProductPageLocators.CART_TITLE_NAME).text
    def same_price(self):
        assert self.browser.find_element(*ProductPageLocators.TITLE_PRICE) in self.browser.find_element(
            *ProductPageLocators.CART_PRICE)
    def solve_quiz_and_get_code(self):
        time.sleep(1)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")