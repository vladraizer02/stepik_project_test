from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_button(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_basket.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "There is no add to cart button"

    def should_be_name_product_in_basket(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_BASKET).text
        assert name_product == name_basket, "The product name does not match the name in the basket"

    def should_be_price_in_basket(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text.split()[2]
        assert price_basket == price_product, "The price of the product does not match the price in the basket"

