from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

        # Product list
        self.products = (By.XPATH, "//div[@class='card h-100']")
        self.product_name = (By.XPATH, ".//div/h4/a")
        self.add_to_cart_button = (By.CSS_SELECTOR, "button.btn-info")

        # Checkout
        self.checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
        self.price_text = (By.CSS_SELECTOR, "td.text-right")
        self.checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

        # Delivery
        self.country_field = (By.ID, "country")
        self.country_options = (By.XPATH, "//div[@class='suggestions']//ul/li/a")
        self.checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.purchase_button = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
        self.success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    # Select a product by name
    def select_product(self, product_to_select):
        products_list = self.driver.find_elements(*self.products)

        # Loop through all options and click the one that matches
        for product in products_list:
            name = product.find_element(*self.product_name).text
            if name == product_to_select:
                print(name)
                product.find_element(*self.add_to_cart_button).click()
                break

    # Verify cart count
    def verify_cart_count(self, expected_count):
        checkout_button = self.driver.find_element(*self.checkout)
        cart_text = checkout_button.text
        assert f"Checkout ( {expected_count} )" in cart_text

    # Verify total price
    def verify_total_amount(self, expected_amount):
        amount_text = self.driver.find_element(*self.price_text).text
        assert str(expected_amount) in amount_text


    # Select country from dropdown
    def select_country(self, country_input, preferred_country):
        # Type into the country input field
        self.driver.find_element(*self.country_field).send_keys(country_input)

        # Wait until all country options are visible
        country_options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='suggestions']//ul/li/a"))
        )

        # Loop through all options and click the one that matches
        for option in country_options:
            if option.text == preferred_country:
                option.click()
                break

    # Agree to terms checkbox
    def agree_terms(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*self.checkbox))
        ).click()


    # Complete purchase and verify success message
    def complete_purchase(self):
        self.driver.find_element(*self.purchase_button).click()
        success_text = self.driver.find_element(*self.success_message).text
        print(success_text)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success_text

    # Full checkout process
    def checkout_process(self, expected_count, expected_amount, country_input, preferred_country):
        self.verify_cart_count(expected_count)
        self.driver.find_element(*self.checkout).click()
        self.driver.save_screenshot(f"Checkout_{int(time.time())}.png")
        self.verify_total_amount(expected_amount)
        self.driver.find_element(*self.checkout_button).click()
        self.select_country(country_input, preferred_country)
        self.agree_terms()
        self.driver.save_screenshot(f"DeliveryPlace_{int(time.time())}.png")
        self.complete_purchase()
        self.driver.save_screenshot(f"Success_{int(time.time())}.png")
