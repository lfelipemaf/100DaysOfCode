from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/", verify=False)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
article_texts = []
article_links = []
articles = soup.find_all(name="a", rel="noreferrer")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_votes = max(article_upvotes)
max_votes_index = article_upvotes.index(max_votes)
print(f"{article_texts[max_votes_index]} - {article_links[max_votes_index]}")