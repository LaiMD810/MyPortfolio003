from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        #Login Page
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.checkbox = (By.ID, "terms")
        self.signIn = (By.CSS_SELECTOR, "input[name='signin']")
        self.dropdown = (By.XPATH,"//select[@class = 'form-control']")

    #Select the User Role
    def select_role_by_value(self, value):
        dropdown = Select(self.driver.find_element(*self.dropdown))
        dropdown.select_by_value(value)

    #Perform Login Action
    def login(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.select_role_by_value("consult")
        self.driver.find_element(*self.checkbox).click()
        self.driver.save_screenshot(f"Loginpage_{int(time.time())}.png")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.signIn)
        ).click()



