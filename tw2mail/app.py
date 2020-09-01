from tw2mail.manage_id import get_sections, get_user_stored_id, store_user_id
from tw2mail.twitter import get_last_tweet, get_user_timeline
from tw2mail.config import create_api

def run():
    api = create_api()

    tw_users = get_sections()
    for user in tw_users:
#        print(str(user))

        last_id = get_user_stored_id (user)
        print (f"Este es es LID: {last_id}")

        if last_id == 0:
            last_id = get_last_tweet(api, user)
            store_user_id(user, last_id)

        get_user_timeline(api, user, last_id)


if __name__ == '__main__':
    run()
