import tweepy
from datetime import datetime
import pandas as pd
import time



consumer_key = 'pTGD1ic97oZd1A66nBNE2LT8r'
consumer_secret = 'A781wWJLIbQwipnBxVyFkYdbkkSqvZRrq3K06OKLLA0EsskRwL'
access_key = '31359324-m0kOgiZIC4KWURaSvWApAW1ksJSiFQffNFSX2leAf'
access_secret = 'ngx7r4GnZiPfc39VTjUbMeY4LLRi5DAVo5KrPgSvRRuOw'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)


def scraptweets(search_words, date_since, numTweets, numRuns):
    
    db_tweets = pd.DataFrame(columns = ['username', 'acctdesc', 'location', 'following',
                                        'followers', 'totaltweets', 'usercreatedts', 'tweetcreatedts',
                                        'retweetcount', 'text', 'hashtags']
                                )
    program_start = time.time()
    for i in range(0, numRuns):
        start_run = time.time()
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(numTweets)
        tweet_list = [tweet for tweet in tweets]
        noTweets = 0
    
    for tweet in tweet_list:
        username = tweet.user.screen_name
        acctdesc = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        usercreatedts = tweet.user.created_at
        tweetcreatedts = tweet.created_at
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
    
    try:
        text = tweet.retweeted_status.full_text
    except AttributeError:  
        text = tweet.full_text
        
        ith_tweet = [username, acctdesc, location, following, followers, totaltweets,
                         usercreatedts, tweetcreatedts, retweetcount, text, hashtags]
        db_tweets.loc[len(db_tweets)] = ith_tweet
        noTweets += 1
        end_run = time.time()
        duration_run = round((end_run-start_run)/60, 2)
        print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
        print('time take for {} run to complete is {} mins'.format(i+1, duration_run))
        time.sleep(920) #15 minute sleep time
        
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
    path = os.getcwd()
    filename = path + '/data/' + to_csv_timestamp + '_sahkprotests_tweets.csv'

    db_tweets.to_csv(filename, index = False)
    program_end = time.time()
    print('Scraping has completed!')
    print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))

search_words = "#covid19 #covid19deaths #covid19recovery"
date_since = "2021-05-01"
numTweets = 10
numRuns = 1
scraptweets(search_words, date_since, numTweets, numRuns)