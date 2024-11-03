from six import text_type
import tweepy

consumer_key = 'pTGD1ic97oZd1A66nBNE2LT8r'
consumer_secret = 'A781wWJLIbQwipnBxVyFkYdbkkSqvZRrq3K06OKLLA0EsskRwL'
access_key = '31359324-m0kOgiZIC4KWURaSvWApAW1ksJSiFQffNFSX2leAf'
access_secret = 'ngx7r4GnZiPfc39VTjUbMeY4LLRi5DAVo5KrPgSvRRuOw'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

print ("This is public TWEETS..............................")
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print ("This is USER TWEETS..............................")
user_tweets = api.user_timeline()
for tweet in user_tweets:
    print(tweet.text)

myuser = api.me()
user = api.get_user(myuser.screen_name)

print ("This is USER FRIENDS")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)
    