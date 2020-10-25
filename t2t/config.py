#!/usr/bin/env python3
import tweepy
import logging
import configparser
import os
#from t2t.local_settings import consumer_key, consumer_secret, access_token, access_token_secret

logger = logging.getLogger()

config_ini = 'config.ini'

def create_api():
    config = configparser.ConfigParser()
    config.read(config_ini)
    auth = tweepy.OAuthHandler(config['DEFAULT']['consumer_key'], config['DEFAULT']['consumer_secret'])
    auth.set_access_token(config['DEFAULT']['access_token'], config['DEFAULT']['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
