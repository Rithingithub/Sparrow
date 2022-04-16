import tweepy


# API keyws that yous saved earlier
api_key = "<API_KEY>"
api_secrets = "<API_SECRET>"
access_token = "<ACCESS_TOKEN>"
access_secret = "<ACCESS_SECRET>"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')
