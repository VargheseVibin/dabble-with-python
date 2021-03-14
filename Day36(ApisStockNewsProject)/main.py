import requests
from twilio.rest import Client

# Stock Price API
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_price_url_key = "*************"
stock_price_url = "https://www.alphavantage.co/query"
stock_alert_threshold = 0.5
UP = "🔺"
DOWN = "🔻"
# example_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

# News API
news_api_url = "https://newsapi.org/v2/everything"
news_api_key = "***********************"
# example_url = "https://newsapi.org/v2/everything?q=Tesla&from=2021-03-13&to=2021-03-13&sortBy=popularity&apiKey=XX"


# Twilio Details
account_sid = "**************************"
auth_token = "***************************"


date_list = []
price_change_pct = 0.0
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def evaluate_stock_price():
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": stock_price_url,
    }
    stock_price_resp = requests.get(url=stock_price_url, params=parameters)
    stock_price_last2days = dict(list(stock_price_resp.json()["Time Series (Daily)"].items())[0:2])
    global date_list
    date_list = [date for date in stock_price_last2days]
    price_today = float(stock_price_last2days[date_list[0]]["4. close"])
    price_yday = float(stock_price_last2days[date_list[1]]["4. close"])
    print(f"Price Today: {price_today}")
    print(f"Price Ysday: {price_yday}")
    global price_change_pct
    price_change_pct = (price_today - price_yday) * 100 / price_yday
    print(price_change_pct)
    # could use abs() function to get the absolute difference
    if price_change_pct ** 2 > stock_alert_threshold ** 2:
        get_stock_news()


def get_stock_news():
    news_params = {
        "q": COMPANY_NAME,
        "from": date_list[1],
        "to": date_list[0],
        "sortBy": "popularity",
        "pageSize": 3,
        "apiKey": news_api_key
    }
    news_api_resp = requests.get(url=news_api_url, params=news_params)
    stock_subj_articles = news_api_resp.json()["articles"][0:3]

    client = Client(account_sid, auth_token)
    if price_change_pct >= 0:
        trend_symbol = UP
    else:
        trend_symbol = DOWN
    for news_item in stock_subj_articles:
        print(f"Title:{news_item['title']}")
        print(f"Brief:{news_item['description']}")
        send_sms_alerts(client, round(price_change_pct,2), trend_symbol, news_item['title'], news_item['description'])


def send_sms_alerts(client, change, trend, title, description):
    message = client.messages \
        .create(
            body=f"{STOCK} {trend} {change}% \n"
                 f"{title} \n"
                 f"{description}",
            from_="+18185321268",
            to="+9179*******61"
    )
    print(message.status)


evaluate_stock_price()

