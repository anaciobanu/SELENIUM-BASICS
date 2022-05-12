from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://automationpractice.com/')
#driver.find_element(By.ID, 'search_query_top').send_keys('dress')
#driver.find_element(By.NAME, 'submit_search').click()
# driver.find_element(By.LINK_TEXT,'Sign in').click()

add_buttons = driver.find_elements(By.CLASS_NAME, "product-container")

print(f'There are {len(add_buttons)} products displayed')

add_buttons[0].click()
driver.find_element(By.NAME, "Submit").click()

print('There is 1 item in your cart' in driver.page_source)

# driver.find_element(By.LINK_TEXT,'Forgot your password?').click()
# print('Retrieve' in driver.page_source)

# driver.find_element(By.LINK_TEXT,'DRESSES').click()
# print('There are 5 products' in driver.page_source)

#add_buttons = driver.find_elements(By.XPATH,"//span[text()='Add to cart']")
# itle='Add to cart']

#print(len(add_buttons))

#sleep(5)

#add_buttons[0].click()