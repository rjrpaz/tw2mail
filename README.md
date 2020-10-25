# Twitter to Telegram gateway

I'm trying to centralize all my sources of information in telegram (RSS, Twitter, etc.).

Sometimes when I check a tweet that has useful information but I have no time to read the link to the article in that moment, I'm forced to add it to "saved tweets" and it will probably die in there.

The goal for this project is to follow the timeline of certain specific Twitter users, check for new tweets, download them and send them to a Telegram channel. That way, the tweets *may die in a telegram channel instead of the "saved tweets" section*.

## Twitter API

This is my main reference to use the Twitter API:

- [https://realpython.com/twitter-bot-python-tweepy/](https://realpython.com/twitter-bot-python-tweepy/)

Follow that guideline to get your Twitter API keys.

This project requires the keys to be stored in file **tw2mail/local_settings.py**. This is a sample content for the file:

```console
mail = 'email_address@domain.com'

consumer_key = 'PUT_YOUR_CONSUMER_KEY_HERE'
consumer_secret = 'PUT_YOUR_CONSUMER_SECRET_HERE'
access_token = 'PUT_YOUR_ACCESS_TOKEN_HERE'
access_token_secret = 'PUT_YOUR_ACCESS_TOKEN_SECRET_HERE'
```

This project also requires a **config.ini** file. This file should include *sections* that define groups of twitter users to be followed. You can define a *subject* for the emails according to the group. Check [config.ini.sample](config.ini.sample) to get an idea.

Twitter still uses some old naming conventions in their API. This are some examples:

- A status is a tweet
- A friendship is a follow-follower relationship
- A favorite is a like
