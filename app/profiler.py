import tweepy

from app.config import Config

class Profiler:
    def __init__(self):
        config = Config()
        CA,CS,AT,AS = config.get_twitter_api_key()
        auth = tweepy.OAuthHandler(CA, CS)
        auth.set_access_token(AT, AS)
        self.api = tweepy.API(auth)


    def get_timeline_users(self):
        user_ids = []
        users = []
        for status in tweepy.Cursor(self.api.home_timeline).items():
            if status.user.id not in user_ids:
                user_ids.append(status.user.id)
                users.append(status.user)
        return users

    def get_followers(self):
        my_info = self.api.me()
        friends_ids = []
        # follower: api.friends_ids -> api.followers_ids
        for friend_id in tweepy.Cursor(self.api.friends_ids, user_id=self.api.me().id).items():
            friends_ids.append(friend_id)

        users = []
        for i in range(0, len(friends_ids), 100):
            for user in self.api.lookup_users(user_ids=friends_ids[i:i+100]):
                users.append(user)

        return users

    def block(self, user_id):
        self.api.create_block(user_id)
