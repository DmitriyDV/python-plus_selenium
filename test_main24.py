import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")
browser.maximize_window()
browser.implicitly_wait(3)

def calc(xxx):
  return str(math.log(abs(12*math.sin(int(xxx)))))

x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
x=x_element.text
y = calc(x)

def test_lesson2():
  button = browser.find_element(By.TAG_NAME, "button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  browser.execute_script("window.scrollBy(0, 100);")
  checkbox = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
  checkbox.click()
  radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  radiobutton.click()
  button_submit = browser.find_element(By.TAG_NAME, "button")
  button_submit.click()
  button.get_attribute()

test_lesson2()
time.sleep(6)

#   // javascript
#   button = document.getElementsByTagName("button")[0];
#   button.scrollIntoView(true);