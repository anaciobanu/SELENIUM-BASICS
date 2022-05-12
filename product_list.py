from math import prod
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('http://automationpractice.com/')

product_list = driver.find_elements(By.CLASS_NAME, "product-name") # this return list of a element

print (len (product_list))

for product in product_list:
    print(product.text)