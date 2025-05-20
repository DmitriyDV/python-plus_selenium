# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import os
# import math
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/redirect_accept.html")
# browser.maximize_window()
# browser.implicitly_wait(3)
import time


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

  # buttonf = browser.find_element(By.XPATH, "//*[@type='submit']")
  # buttonf.click()
  #
  # confirm = browser.switch_to.alert
  # confirm.accept()
  #
  # def calc(xxx):
  #   return str(math.log(abs(12 * math.sin(int(xxx)))))
  #
  # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  # x = x_element.text
  # y = calc(x)
  #
  # enterfield = browser.find_element(By.CSS_SELECTOR, "#answer")
  # enterfield.send_keys(y)

#   buttonf1 = browser.find_element(By.XPATH, "//*[@type='submit']")
#   buttonf1.click()
#
#   new_window = browser.window_handles[1]
#   browser.switch_to.window(new_window)
#
#   def calc(xxx):
#     return str(math.log(abs(12 * math.sin(int(xxx)))))
#
#   x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#   x = x_element.text
#   y = calc(x)
#
#   enterfield = browser.find_element(By.CSS_SELECTOR, "#answer")
#   enterfield.send_keys(y)
#
#   buttonf1 = browser.find_element(By.XPATH, "//*[@type='submit']")
#   buttonf1.click()
#
# test_lesson()
# time.sleep(6)

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

# browser.switch_to.window(window_name)

# new_window = browser.window_handles[1] # получить имя второй вкладки
# first_window = browser.window_handles[0] # имя текущей вкладки

  # from selenium import webdriver
  # from selenium.webdriver.common.by import By
  #
  # browser = webdriver.Chrome()
  # browser.implicitly_wait(5)
  # browser.get("http://suninjuly.github.io/wait1.html")
  #
  # button = browser.find_element(By.ID, "verify")
  # button.click()
  # message = browser.find_element(By.ID, "verify_message")
  #
  # assert "successful" in message.text

  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium import webdriver

  browser = webdriver.Chrome()

  browser.get("http://suninjuly.github.io/wait2.html")

  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
  button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify"))
  )
  button.click()
  message = browser.find_element(By.ID, "verify_message")

  assert "successful" in message.text

  # В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:
  #
  # title_is
  # title_contains
  # presence_of_element_located
  # visibility_of_element_located
  # visibility_of
  # presence_of_all_elements_located
  # text_to_be_present_in_element
  # text_to_be_present_in_element_value
  # frame_to_be_available_and_switch_to_it
  # invisibility_of_element_located
  # element_to_be_clickable
  # staleness_of
  # element_to_be_selected
  # element_located_to_be_selected
  # element_selection_state_to_be
  # element_located_selection_state_to_be
  # alert_is_present

  # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
  # button = WebDriverWait(browser, 5).until_not(
  #   EC.element_to_be_clickable((By.ID, "verify"))
  # )