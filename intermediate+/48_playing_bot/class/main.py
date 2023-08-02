from selenium import webdriver

chrome_driver_path = "/Users/picpay/PycharmProjects/chromedriver"
driver = webdriver.Chrome()

# driver.get("https://www.amazon.com.br/dp/140954947X/?coliid=IDEY054C1IRHK&colid=F47WVX7JHT6C&psc=1&ref_=list_c_wl_lv_ov_lig_dp_it")
# price = float(driver.find_element("id", "price").text.split("R$")[1].replace(",", "."))
# print(price)

driver.get("https://www.python.org/")
search_bar = driver.find_element("name", "q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element("python-logo")
print(logo.size)

documentation = driver.find_elements(value=".documentation-widget a")
print(documentation)
driver.quit()