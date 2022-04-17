#SparrowTeambot -Twitter Bot

import requests
import keys
import pandas as pd
import tweepy
import time

def get_crypto_rates(base_currency='INR', assets='BTC,ETH,XRP'):
        url = 'https://api.nomics.com/v1/currencies/ticker'
        payload = {'key': keys.API_KEY1, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
        response = requests.get(url, params=payload)
        data = response.json()
        crypto_currency, crypto_price, crypto_timestamp = [], [], []

        #print(data)
        for asset in data:
            crypto_currency.append(asset['currency'])
            crypto_price.append(asset['price'])
            crypto_timestamp.append(asset['price_timestamp'])

        raw_data = {
            'Assets': crypto_currency,
            'Rate': crypto_price,
            'Timestamp': crypto_timestamp
        }

        df = pd.DataFrame(raw_data)
        print(df)
        return df.to_string()

while(True):




    res=get_crypto_rates()


    client = tweepy.Client(bearer_token=keys.bearer_token,
                           consumer_key=keys.consumer_key,
                           consumer_secret=keys.consumer_secret,
                           access_token=keys.access_token,
                           access_token_secret=keys.access_token_secret)
    client.create_tweet(text=res,user_auth=True)
    print("Waiting 60 Minute...")
    time.sleep(3600) #runs hourly

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
