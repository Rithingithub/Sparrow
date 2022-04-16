import tweepy


# API keyws that yous saved earlier
api_key = "RSZjBFIKELSmycKKB9rvXLtp9"
api_secrets = "IF1haNyRkHsaQb5tFtIcT2kpojmUfgYlslhLdys7J3m9qRvUQG"
access_token = "1515311399878422542-9IuvjqLtrc7rqGgxgrHg3HTHT7LmrC"
access_secret = "1N52oC1djy7Atrvf79KG2WRwDzbCD5sqkYfT8yiuUjtMV"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secrets)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')