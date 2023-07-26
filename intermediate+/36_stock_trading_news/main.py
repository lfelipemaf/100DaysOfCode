from creds import *
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&"
                            f"apikey={alpha_vantage_key}", verify=False)
response.raise_for_status()
data = response.json()
d1 = str(dt.datetime.today() - dt.timedelta(days=1)).split(" ")[0]
d2 = str(dt.datetime.today() - dt.timedelta(days=2)).split(" ")[0]

y = float(data["Time Series (Daily)"][d1]["4. close"])
dby = float(data["Time Series (Daily)"][d2]["4. close"])

diff = y-dby
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

delta = (diff/ dby) * 100

if abs(delta) > 0:
    response = requests.get(url=f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={news_api_key}", verify=False)
    response.raise_for_status()
    news_data = response.json()["all_movies"]

    three_articles = news_data[:3]

    formatted_articles = [f"{STOCK} - {up_down}{round(delta)}%\nHeadline: {article['title']}.\nBrif: {article['description']}" for article in three_articles]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles:

    message = client.messages \
                    .create(
                         body=article,
                         from_=twilio_from,
                         to=my_number
                     )
    print(message.sid)
