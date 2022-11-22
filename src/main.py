# Send a tweet every 1 second
from tweeter_api import send_tweet
import datetime as dt
import time

start_time = time.time()


def tweet():
    message = f"This tweet is sent at :\nDate   : {dt.datetime.now().date()}\nTime   : {dt.datetime.now().time()} (WIB)" \
              f"\n\nThis tweet is sent by a bot"

    send_tweet(message, "image.jpg")


lim = int(input("Tweet Limit : "))
counter = 0
delay = float(input("Delay : "))

while counter < lim:
    tweet()
    counter += 1
    time.sleep(delay - ((time.time() - start_time) % delay))


