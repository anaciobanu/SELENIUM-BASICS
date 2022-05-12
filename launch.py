from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get ('https://www.google.com/')

driver.maximize_window()
driver.get ('https://www.yahoo.com/')

driver.back()
driver.forward()
driver.minimize_window()
driver.close()

