from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/", verify=False)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

article_tag = soup.find(name="a", rel="noreferrer")

article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score").getText()
print(f"{article_text} - {article_link} - {article_upvote}")