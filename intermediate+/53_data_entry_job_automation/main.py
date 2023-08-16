import requests
from bs4 import BeautifulSoup
import lxml

forms_link = "https://forms.gle/m98mqNyFuRoDBVyP8"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(
    "https://www.zillow.com/toronto-on/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A44.67304353029494%2C%22east%22%3A-77.50184226367188%2C%22south%22%3A42.678897619351%2C%22west%22%3A-81.06690574023438%7D%2C%22usersSearchTerm%22%3A%22Toronto%20ON%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A483559%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2600%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22schm%22%3A%7B%22value%22%3Afalse%7D%2C%22schh%22%3A%7B%22value%22%3Afalse%7D%2C%22schu%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22schp%22%3A%7B%22value%22%3Afalse%7D%2C%22schr%22%3A%7B%22value%22%3Afalse%7D%2C%22sche%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22schc%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22featured%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D",
    headers=header, verify=False)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select("ul li div div a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
all_address_elements = soup.select("ul li div div a address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
all_price_elements = soup.select('div > div.StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0.bKpguY.property-card-data > div.StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0.fDSTNn > div > span')
print(all_price_elements)
all_prices = []
for price in all_price_elements:
    a = price.getText()
    print(a)
    all_prices.append(a)


print(all_addresses)
print(all_prices)
print(all_links)