import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")
browser.maximize_window()
browser.implicitly_wait(3)

def calc(xxx):
  return str(math.log(abs(12*math.sin(int(xxx)))))

# x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
# x=x_element.text
# y = calc(x)

def test_lesson2():
  # browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

  # icon_img = browser.find_element(By.XPATH,"//img")
  # icon_img_attr = icon_img.get_attribute("valuex")
  # print(icon_img_attr)
  # y = calc(icon_img_attr)
  # browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  # checkbox = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
  # checkbox.click()
  # radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
  # radiobutton.click()
  # button_submit = browser.find_element(By.TAG_NAME, "button")
  # button_submit.click()

  first_integer = browser.find_element(By.CSS_SELECTOR,"#num1")
  f1 = int(first_integer.text)
  second_integer = browser.find_element(By.CSS_SELECTOR,"#num2")
  f2 = int(second_integer.text)
  sum = f1 + f2

  select = Select(browser.find_element(By.TAG_NAME, "select"))
  print(sum)
  time.sleep(1)
  vl = str(sum)
  select.select_by_value(vl)
  button_submit = browser.find_element(By.TAG_NAME, "button")
  button_submit.click()

test_lesson2()
time.sleep(6)