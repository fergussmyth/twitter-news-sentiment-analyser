import tweepy

def authenticate_twitter_api():
    consumer_key = "7MvYZ1fcspuMvNBkDYSotNl5x"
    consumer_secret = "22Sg8deUvOaMd8DqouIYUKQ9mN68os6N7FUEAANTBwn8IgYSQ0"
    access_token = "1674436723755950081-5gQqkcqdubWx6TmzIUKBFBxCYXtpn2"
    access_token_secret = "ctH82aARhG2W6gOvaNMvU11tEL73JcMibrOIvSIBDlq7d"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api