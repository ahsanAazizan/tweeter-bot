# Requirement : tweepy library installed
import tweepy
import secrets


def api_auth():
    auth = tweepy.OAuthHandler(consumer_key=secrets.API_KEY, consumer_secret=secrets.API_KEY_SECRET)
    auth.set_access_token(key=secrets.ACCESS_TOKEN, secret=secrets.ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)


# Method to send tweets: message
def send_tweet(message: str, image_path=None):
    api = api_auth()
    if image_path is not None:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweet send successfully')


