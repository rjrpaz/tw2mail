# Twitter to email gateway

I'm a big fan of using my email interface as a my own personal portal, so I always try to centralize all my sources of information there (RSS, p.e.).

Sometimes when I check a tweet that has useful information but I have no time to read the link to the article in that moment, I'm forced to add the tweet to "saved tweets" and it will probably die in there.

The goal for this project is to follow the timeline of certain specific Twitter users, check for new tweets, download them and send them by email to my own personal account. That way, the tweets may die in a mail folder instead of the "saved tweets" section.

## Twitter API

This are my references to interact with the Twitter API:

- [https://realpython.com/twitter-bot-python-tweepy/](https://realpython.com/twitter-bot-python-tweepy/)

Twitter still uses some old naming conventions in their API. This are some examples:

- A status is a tweet
- A friendship is a follow-follower relationship
- A favorite is a like
