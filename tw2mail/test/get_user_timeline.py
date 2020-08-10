#!/usr/bin/env python3
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_user_timeline(api, screen_name):
    logger.info(f"Retrieving user {screen_name} timeline")
    counter = 1
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=10, page=1).items():
        print (counter)
        print (tweet.text)
        counter = counter + 1

    return

def main():
    api = create_api()
    screen_name = 'infobae'
    get_user_timeline(api, screen_name)

if __name__ == "__main__":
    main()