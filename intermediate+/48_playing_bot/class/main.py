from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.amazon.com.br/dp/140954947X/?coliid=IDEY054C1IRHK&colid=F47WVX7JHT6C&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it")
# price = float(driver.find_element("id", "price").text.split("R$")[1].replace(",", "."))
# print(price)

driver.get("https://www.python.org/")
# search_bar = driver.find_element("name", "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)

# xpath = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/a')
# print(xpath.text)

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_title = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
event_dict = {}
for i in range(len(event_time)):
    event_dict[i] = {
        "time": event_time[i].text,
        "name": event_title[i].text,
    }

print(event_dict)


driver.quit()
