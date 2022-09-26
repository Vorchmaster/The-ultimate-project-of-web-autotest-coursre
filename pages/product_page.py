from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
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
            #time.sleep(100)
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "There is no product name"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "There is no product price"

    def check_addded_product_name(self):
        self.browser.implicitly_wait(10)
        element1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        element2 = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_NAME)
        assert element1.text == element2.text, "Invalid product name alerted"

    def check_addded_product_price(self):
        self.browser.implicitly_wait(10)
        element1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        element2 = self.browser.find_element(*ProductPageLocators.PRODUCT_ALERT_PRICE)
        assert element1.text == element2.text, "Invalid product price alerted"

