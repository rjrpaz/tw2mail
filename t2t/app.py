from t2t.manage_id import list_tw_users
from t2t.twitter import get_last_tweet, get_tweets
from t2t.config import create_api
import logging
from t2t import telegram

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
#logger.disabled = False
logger.disabled = True

def run():
    api = create_api()

    tw_users = list_tw_users()
    for user in tw_users:
        logger.info(f"Stored ID for user {user.tag} is {user.last_id}")

        if user.last_id == 0:
            last_id = get_last_tweet(api, user)
            user.store_id(last_id)

        max_id = 0
        tweets = get_tweets(api, user.tag, user.last_id)
        for tweet in tweets:
            logger.info(f"Tweet: {tweet.text}")
            telegram.send_message(user.tag, user.channel_id, tweet)
            if tweet.id > max_id:
                max_id = tweet.id

        if int(user.last_id) < max_id:
            user.store_id(max_id)
            logger.info(f"New ID for user {user.tag} is {max_id}")
        else:
            logger.info(f"No new tweets for user {user.tag}")

if __name__ == '__main__':
    run()
