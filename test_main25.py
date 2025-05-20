import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
browser.maximize_window()
browser.implicitly_wait(3)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

def test_lesson():
  firstname = browser.find_element(By.XPATH, "//*[@name='firstname']")
  firstname.send_keys("fname")
  lastname = browser.find_element(By.XPATH, "//*[@name='lastname']")
  lastname.send_keys("lname")
  mail = browser.find_element(By.XPATH, "//*[@name='email']")
  mail.send_keys("email@name")
  filebutton = browser.find_element(By.XPATH, "//*[@id='file']")
  filebutton.send_keys(file_path)
  button_submit = browser.find_element(By.TAG_NAME, "button")
  button_submit.click()

test_lesson()
time.sleep(6)

#   // javascript
#   button = document.getElementsByTagName("button")[0];
#   button.scrollIntoView(true);

