import requests
import keys
import pandas as pd
import tweepy
import os



def get_crypto_rates(base_currency='INR', assets='BTC,ETH,XRP'):
    url = 'https://api.nomics.com/v1/currencies/ticker'
    payload = {'key': keys.API_KEY1, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
    response = requests.get(url, params=payload)
    data = response.json()

    crypto_currency, crypto_price, crypto_timestamp = [], [], []

    print(data)
    for asset in data:
        crypto_currency.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])

    raw_data = {
        'assets': crypto_currency,
        'Rate': crypto_price,
        'timestamp': crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df


get_crypto_rates()


API_KEY = '4pDsoT0NHXFOtRdVGE6nq2YxB'
API_SECRET = 'Tupz8N2nlnkMSZXlXN08SoakvVTtVjfQToKAxnAIRZBVR1EIWe'
#API_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAME6bgEAAAAAJH7a4LsF%2BQQXk5EDcXNtEdM3xyw%3Dzg5H5F3iQerDWWMcgw3WUqTLiTO1epU5DYRxekVGHHDx5ejxHc'
ACCESS_TOKEN = '1515311399878422542-9IuvjqLtrc7rqGgxgrHg3HTHT7LmrC'
ACCESS_SECRET = '1N52oC1djy7Atrvf79KG2WRwDzbCD5sqkYfT8yiuUjtMV'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#tweet_list = api.favorites(screen_name='rithin_lehan', count=5)
#print(tweet_list)

api.update_status(status="Welcome Twitter ")
