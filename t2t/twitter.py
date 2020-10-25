#!/usr/bin/env python3
import tweepy
import logging
from t2t.config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
MAX_TWEETS = 20

class Tweet:
    def __init__(self):
        self.text = []
        self.id = 0

def get_last_tweet(api, screen_name):
    logger.info(f"Retrieving last tweet from user {screen_name}")
    tweet = api.user_timeline(screen_name=screen_name, page=1)[0]

    return tweet.id

def get_tweets(api, screen_name, since_id):
    logger.info(f"Retrieving user {screen_name} timeline")
    max_id = since_id
    list = []
    results = [status._json for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, since_id=since_id, count=1000, tweet_mode='extended', lang='en').items()]
    total_tweets = 0
    for result in reversed(results):
        t = Tweet()
        t.text = result["full_text"]
        t.id = result["id"]
        list.append(t)
        total_tweets = total_tweets + 1
        if total_tweets >= MAX_TWEETS:
            break

    return list
