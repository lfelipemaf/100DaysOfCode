import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com.br/dp/B0949DC5H6/?coliid=I3QQ0I3WFEI18W&colid=F47WVX7JHT6C&psc=1&ref_=list_c_wl_gv_ov_lig_pi_dp"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"
}
target_price = 62.00

response = requests.get(url=URL, headers=headers, verify=False)

soup = BeautifulSoup(response.content, "lxml")
price = float(soup.find(class_="a-offscreen").getText().split("R$")[1].replace(",", "."))
product_title = soup.find(id="productTitle").getText()
if price <= target_price:
    print(f"PRICE ALERT\n\n"
          f"The {product_title} you are looking for to buy is now R${str(price).replace('.',',')}\n\n"
          f"Get it right now: {URL}")
