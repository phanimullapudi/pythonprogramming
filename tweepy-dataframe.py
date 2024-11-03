import tweepy
from datetime import datetime
import pandas as pd
import time
import os

consumer_key = 'pTGD1ic97oZd1A66nBNE2LT8r'
consumer_secret = 'A781wWJLIbQwipnBxVyFkYdbkkSqvZRrq3K06OKLLA0EsskRwL'
access_key = '31359324-m0kOgiZIC4KWURaSvWApAW1ksJSiFQffNFSX2leAf'
access_secret = 'ngx7r4GnZiPfc39VTjUbMeY4LLRi5DAVo5KrPgSvRRuOw'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

myuser = api.me()
user = api.get_user(myuser.screen_name)

db_users = pd.DataFrame(columns = ['screen_name', 'id'])


to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
path = os.getcwd()
filename = path + '/data/' + to_csv_timestamp + '_userfollowing.csv'
db_users = user.friends()

db_users.to_csv(filename, index = False)

for friend in user.friends():
   print(friend.screen_name, friend.id)
    