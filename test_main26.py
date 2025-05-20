import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.maximize_window()
browser.implicitly_wait(3)

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

def test_lesson():
  # firstname = browser.find_element(By.XPATH, "//*[@name='firstname']")
  # firstname.send_keys("fname")
  # lastname = browser.find_element(By.XPATH, "//*[@name='lastname']")
  # lastname.send_keys("lname")
  # mail = browser.find_element(By.XPATH, "//*[@name='email']")
  # mail.send_keys("email@name")
  # filebutton = browser.find_element(By.XPATH, "//*[@id='file']")
  # filebutton.send_keys(file_path)
  # button_submit = browser.find_element(By.TAG_NAME, "button")
  # button_submit.click()

  buttonf = browser.find_element(By.XPATH, "//*[@type='submit']")
  buttonf.click()

  confirm = browser.switch_to.alert
  confirm.accept()

  def calc(xxx):
    return str(math.log(abs(12 * math.sin(int(xxx)))))

  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)

  enterfield = browser.find_element(By.CSS_SELECTOR, "#answer")
  enterfield.send_keys(y)

  buttonf2 = browser.find_element(By.XPATH, "//*[@type='submit']")
  buttonf2.click()

test_lesson()
time.sleep(6)

#   // javascript
#   button = document.getElementsByTagName("button")[0];
#   button.scrollIntoView(true);

# alert = browser.switch_to.alert
# alert.accept()

# alert = browser.switch_to.alert
# alert_text = alert.text

# confirm = browser.switch_to.alert
# confirm.accept()

# confirm.dismiss()

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()