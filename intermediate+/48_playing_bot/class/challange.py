from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# # all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
btn = driver.find_element(By.TAG_NAME, "button")

first_name.send_keys("Felipe")
last_name.send_keys("Moriondo")
email.send_keys('lfelipemaf@icloud.com')
btn.click()
time.sleep(10)
# driver.quit()
