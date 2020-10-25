# Twitter to Telegram gateway

I'm trying to centralize all my sources of information in telegram (RSS, Twitter, etc.).

Sometimes when I check a tweet that has useful information but I have no time to read the link to the article in that moment, I'm forced to add it to "saved tweets" and it will probably die in there.

The goal for this project is to follow the timeline of certain specific Twitter users, check for new tweets, download them and send them to a Telegram channel. That way, the tweets *may die in a telegram channel instead of the "saved tweets" section*.

## Config file

This project requires the keys to be stored in **config.ini** file. This is a sample content for the file:

```console
[DEFAULT]
# Required for Telegram authentication
bot_token = PUT_YOUR_TELEGRAM_TOKEN_HERE
# Required for Twitter authentication
consumer_key = PUT_YOUR_CONSUMER_KEY_HERE
consumer_secret = PUT_YOUR_CONSUMER_SECRET_HERE
access_token = PUT_YOUR_ACCESS_TOKEN_HERE
access_token_secret = PUT_YOUR_ACCESS_TOKEN_SECRET_HERE

[CHANNELS]
news = id_for_telegram_channel

[infobae]
last_id = 1320348776662500101
channel_id = ${CHANNELS:news}
```

**DEFAULT** section includes all the information required to do authentication to Twitter and Telegram.

**CHANNELS** section includes all the id for every telegram channel.

The following sections define the twitter users to be followed.

Check [config.ini.sample](config.ini.sample) to get an idea.

## Twitter API

This is my main reference to use the Twitter API:

- [https://realpython.com/twitter-bot-python-tweepy/](https://realpython.com/twitter-bot-python-tweepy/)

Follow that guideline to get your Twitter API keys.

Twitter still uses some old naming conventions in their API. This are some examples:

- A status is a tweet
- A friendship is a follow-follower relationship
- A favorite is a like

## Telegram API

Creation of public or private Telegram channel to upload the message goes beyond the scope of this document. You can check some guidelines here:

[https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd](https://medium.com/@ljmocic/make-telegram-bot-for-notifying-about-new-rss-feed-items-4cfbcc37f4fd)

- *token* is obtained after the bot's creation
- *channel id* can be obtained from channel information
