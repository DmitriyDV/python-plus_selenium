import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('links',["236895",
                                "236896",
                                "236897",
                                  "236898",
                                  "236899",
                                  "236903",
                                  "236904",
                                  "236905"])
def test_me_should_login_and_dont_see_pop_up(browser,links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)

    button_login = browser.find_element(By.CSS_SELECTOR,"#ember478")
    button_login.click()

    login_field = browser.find_element(By.CSS_SELECTOR,"#id_login_email")
    login_field.send_keys("")
    password_field = browser.find_element(By.CSS_SELECTOR,"#id_login_password")
    password_field.send_keys("")
    button_send = browser.find_element(By.CSS_SELECTOR,".button_with-loader")
    button_send.click()

    wait_vis_btn = WebDriverWait(browser,5)
    wait_vis_btn.until(EC.invisibility_of_element_located(button_send))
    field_send = browser.find_element(By.XPATH,"//*[@placeholder='Напишите ваш ответ здесь...']")
    field_send2 = WebDriverWait(browser,10).until(
        EC.element_to_be_selected(field_send)
    )
    field_send2.clear()
    field_send.send_keys(str(math.log(int(time.time()))))

    btn_snd = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    btn_snd.click()
    wait = WebDriverWait(browser, 10)
    check_m = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    check = check_m.text
    assert check == "Correct!", f"{check}"