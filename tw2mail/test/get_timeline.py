#!/usr/bin/env python3
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def get_timeline(api, since_id):
    logger.info("Retrieving timeline")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.home_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        print (tweet.text)

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = get_timeline(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()