import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LoginPage import LoginPage
from product_page import ProductPage

options = webdriver.ChromeOptions()
options.add_argument("--incognito")   # create option that run in private mode


driver = webdriver.Chrome(options=options) #make the chromedriver to use created options
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
response = requests.get("https://rahulshettyacademy.com/loginpagePractise/")
print("Response Status Code:", response.status_code)

loginPage = LoginPage(driver)
loginPage.login("rahulshettyacademy","Learning@830$3mK2")

print("Login successfully")


productPage = ProductPage(driver)
productPage.select_product("Samsung Note 8")
productPage.checkout_process(1,85000,"In","India")




driver.quit()