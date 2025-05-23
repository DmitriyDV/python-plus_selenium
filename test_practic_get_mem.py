from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://9gag.com/trending")
driver.implicitly_wait(5)
f_mem = driver.find_element(By.CLASS_NAME, "badge-evt")
f_mem_link = f_mem.get_attribute("href")

with open('meme.txt','w') as meme_file:
    meme_file.write(f_mem_link)