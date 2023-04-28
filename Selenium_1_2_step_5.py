Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... from selenium.webdriver.common.by import By
... import time
... 
... 
... link = "https://suninjuly.github.io/math.html"
... browser = webdriver.Chrome()
... browser.get(link)
... 
... import math
... 
... def calc(x):
...     return str(math.log(abs(12*math.sin(int(x)))))
... 
... x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
... x = x_element.text
... 
... input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
... input1.send_keys(calc(x))
... 
... option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
... option1.click()
... option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
... option2.click()
... 
... button = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
... button.click()
... 
... time.sleep(10)
... browser.quit()
