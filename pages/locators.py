from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "[href='/en-gb/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    REGISTR_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    EMAIL_REG = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_REG = (By.CSS_SELECTOR, "#id_registration-password1")
    CONF_PASSWORD_REG = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div>h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, ".hidden-xs")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasketPageLocators():
    BASKET_NOT_PRODUCTS = (By.CSS_SELECTOR, ".row>h2")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")