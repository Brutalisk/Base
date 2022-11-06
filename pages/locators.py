from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form")
class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_basket_form")
    TITLE_NAME = (By.CSS_SELECTOR, "#div.col-sm-6.product_main.h1")
    CART_TITLE_NAME = (By.CSS_SELECTOR, "#div.alertinner.strong")
    TITLE_PRICE = (By.CSS_SELECTOR, "#div.col-sm-6.product_main.p:nth-child(2)")
    CART_PRICE = (By.XPATH, "//div/p/strong[text()]")