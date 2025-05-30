import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
button = browser.find_element(By.ID,"book")
button.click()

def calc(xxx):
    return str(math.log(abs(12*math.sin(int(xxx)))))

x_element = browser.find_element(By.CSS_SELECTOR,"#input_value")
x=x_element.text
y = calc(x)

entertext = browser.find_element(By.CSS_SELECTOR, "#answer")
entertext.send_keys(y)

buttonsend = browser.find_element(By.CSS_SELECTOR,"#solve")
buttonsend.click()
time.sleep(9)
