from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET), "Basket link is not presented"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_PRODUCTS), "There are products in the basket"

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "The basket is not empty"