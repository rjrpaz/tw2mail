from t2t.manage_id import get_sections, get_user_stored_id, store_user_id
from t2t.twitter import get_last_tweet, get_user_timeline
from t2t.config import create_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
#logger.disabled = False
logger.disabled = True

def run():
    api = create_api()

    tw_users = get_sections()
    for user in tw_users:
        last_id = get_user_stored_id (user)
        logger.info(f"Stored ID for user {user} is {last_id}")

        if last_id == 0:
            last_id = get_last_tweet(api, user)
            store_user_id(user, last_id)

        Tweet_info = get_user_timeline(api, user, last_id)
        if last_id != Tweet_info.max_id:
            logger.info("Latest tweets:")
#            for tweet in Tweet_info.tweets:
#                print(tweet)
        
            store_user_id(user, Tweet_info.max_id)
            logger.info(f"New ID for user {user} is {Tweet_info.max_id}")
        else:
            logger.info(f"No new tweets for user {user}")

if __name__ == '__main__':
    run()
