import requests
from twilio.rest import Client
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

two_days_ago = dt.datetime.now() - dt.timedelta(days=2)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

stocks_params = {
  "apikey": "R35LRZ3SIR19NP3M",
  "symbol": STOCK,
  "function": "TIME_SERIES_WEEKLY",
}

response = requests.get(url=STOCK_ENDPOINT, params=stocks_params)
data = response.json()["Weekly Time Series"]
data_list = [el for (key, el) in data.items()]
yesterday_price = data_list[0]["4. close"]
before_yesterday_price = data_list[1]["4. close"]

difference = float(yesterday_price) - float(before_yesterday_price)
difference_percent = round((difference / float(before_yesterday_price)) * 100)




## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator

if abs(difference_percent) > 1:
  news_params = {
    "api_key": "ba18924ac15647ef9ac2374bf7191432",
    "q": "tesla",
    "sortBy": "published",
    "from": two_days_ago.two_days_ago.strftime("%Y-%m-%d")
  }

  response = requests.get(url=NEWS_ENDPOINT, params=news_params)
  articles = response.json()["articles"]
  latest_articles = articles[:3]
  formatted_articles = [f"{STOCK}: \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in latest_articles]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

