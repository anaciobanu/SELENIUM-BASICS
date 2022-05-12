from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
print(driver.title)
print(driver.name)
print(driver.current_url)

print('Accepted usernames' in driver.page_source)