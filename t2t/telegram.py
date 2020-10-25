import requests
import html
import re
import configparser
from t2t.twitter import Tweet


config_ini = 'config.ini'

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def send_message(tag, channel_id, tweet: Tweet):
	config = configparser.ConfigParser()
	config.read(config_ini)

	link = 'https://twitter.com/' + tag + '/status/' + str(tweet.id)
	message = '\n'.join([link, tweet.text])
	requests.get(f'https://api.telegram.org/bot{config["DEFAULT"]["bot_token"]}/sendMessage?chat_id={channel_id}&text={message}')
