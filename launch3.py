from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://getbootstrap.com/docs/5.0/forms/checks-radios/')
driver.maximize_window()


# default_checkbox = driver.find_element(By.CSS_SELECTOR, '#flexCheckDefault')
# driver.execute_script('arguments[0].click()', default_checkbox)

# disabled_checkbox = driver.find_element(By.CSS_SELECTOR, '#flexCheckDisabled')
# driver.execute_script('arguments[0].scrollIntoView(true)', disabled_checkbox)
# print(not disabled_checkbox.is_selected())
# print(disabled_checkbox.is_displayed())
# print(not disabled_checkbox.is_enabled())

default_radio1 = driver.find_element(By.CSS_SELECTOR, '#flexRadioDefault1')
default_radio2 = driver.find_element(By.CSS_SELECTOR, '#flexRadioDefault2')
driver.execute_script('arguments[0].scrollIntoView(true)', default_radio1)

print(default_radio1.is_selected())
print(default_radio2.is_selected())

# default_radio1.click()

driver.execute_script('arguments[0].click()', default_radio1)

print(default_radio1.is_selected())
print(default_radio2.is_selected())