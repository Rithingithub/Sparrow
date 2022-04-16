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


API_KEY = '<API_KEY>'
API_SECRET = '<API_SECRET>'
#API_TOKEN = '<API_TOKEN>'
ACCESS_TOKEN = '<ACCESS_KEY>'
ACCESS_SECRET = '<ACCESS_SECRET>'


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

#tweet_list = api.favorites(screen_name='rithin_lehan', count=5)
#print(tweet_list)

api.update_status(status="Welcome Twitter ")


#Retweet
for tweet in api.favorite(screen_name='Bitcoin'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)

for tweet in api.favorite(screen_name='ethereum'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)

for tweet in api.favorite(screen_name='XRPcryptowolf'):
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)
