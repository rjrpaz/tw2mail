#!/usr/bin/env python3
import tweepy
import logging
from tw2mail.config import create_api
from tw2mail.manage_id import get_sections, get_user_stored_id
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_last_tweet(api, screen_name):
    logger.info(f"Retrieving last tweed from user {screen_name}")
    tweet = api.user_timeline(screen_name=screen_name, page=1)[0]

    return tweet.id

def get_user_timeline(api, screen_name, since_id):
    logger.info(f"Retrieving user {screen_name} timeline")
    counter = 1
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=screen_name, since_id=since_id, count=20, page=1).items():
        print (counter)
        print (tweet.text)
        counter = counter + 1

    return
