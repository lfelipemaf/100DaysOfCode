import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL, verify=False)

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
article_texts = []
articles = soup.find_all(name="h3", class_="title")
for article_tag in articles:
    text = article_tag.getText()
    article_texts.insert(0,text)

with open("movie_list.txt", "w") as file:
    for movie in article_texts:
        file.write(movie)
        file.write("\n")

