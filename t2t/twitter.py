#!/usr/bin/env python3
import tweepy
import logging
from t2t.config import create_api
from t2t.manage_id import get_sections, get_user_stored_id
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Tweet_info:
    def __init__(self):
        self.tweets = []
        self.max_id = 0


def get_last_tweet(api, screen_name):
    logger.info(f"Retrieving last tweet from user {screen_name}")
    tweet = api.user_timeline(screen_name=screen_name, page=1)[0]

    return tweet.id

def get_user_timeline(api, screen_name, since_id):
    logger.info(f"Retrieving user {screen_name} timeline")
    max_id = since_id
    Tweet_info.tweets = []
    results = [status._json for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, since_id=since_id, count=1000, tweet_mode='extended', lang='en').items()]
    for result in results:
        Tweet_info.tweets.append(result["full_text"])
        print(f"Tweet: {result['full_text']}")

        if result["id"] > max_id:
            max_id = result["id"]

    Tweet_info.max_id = max_id
    return Tweet_info
