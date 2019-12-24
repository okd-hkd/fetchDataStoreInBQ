
from dotenv import load_dotenv, find_dotenv
import os
import math

load_dotenv()
load_dotenv(find_dotenv())

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("OAUTH_TOKEN")
access_token_secret = os.getenv("OAUTH_TOKEN_SECRET")

import tweepy

# Search tweets.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = tweepy.Cursor(api.search, q='地震', lang='ja').items(100)

import json
from datetime import datetime

# Write tweets to json file.
filename = 'tweets_{}.json'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
with open(filename, 'w', encoding="utf-8") as f:
    for tweet in tweets:
        importance_index = round(tweet.retweet_count * 1.0 + tweet.favorite_count * 0.1)
        dic = {'text': tweet.text,
               'date': str(tweet.created_at),
               'id': tweet.id,
               'user_id':tweet.user.id,
              #  'created_at':tweet.created_at,
               'retweet_count':tweet.retweet_count,
               'favorite_count':tweet.favorite_count,
               'importance_index': importance_index
               }

        json.dump(dic, f, ensure_ascii=False)
        f.write('\n')