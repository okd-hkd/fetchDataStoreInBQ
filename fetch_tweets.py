# coding: utf-8

from dotenv import load_dotenv, find_dotenv
import os
import math
import time


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
tweets = tweepy.Cursor(api.search, q='??', lang='ja').items(10)

# Parameters:	

# q – the search query string of 500 characters maximum, including operators. Queries may additionally be limited by complexity.
# geocode – Returns tweets by users located within a given radius of the given latitude/longitude. The location is preferentially taking from the Geotagging API, but will fall back to their Twitter profile. The parameter value is specified by “latitide,longitude,radius”, where radius units must be specified as either “mi” (miles) or “km” (kilometers). Note that you cannot use the near operator via the API to geocode arbitrary locations; however you can use this geocode parameter to search near geocodes directly. A maximum of 1,000 distinct “sub-regions” will be considered when using the radius modifier.
# lang – Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.
# locale – Specify the language of the query you are sending (only ja is currently effective). This is intended for language-specific consumers and the default should work in the majority of cases.
# result_type –

# Specifies what type of search results you would prefer to receive. 
# The current default is “mixed.” Valid values include:
# mixed : include both popular and real time results in the response
# recent : return only the most recent results in the response
# popular : return only the most popular results in the response

# count – The number of results to try and retrieve per page.
# until – Returns tweets created before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index has a 7-day limit. In other words, no tweets will be found for a date older than one week.
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets which can be accessed through the API. If the limit of Tweets has occurred since the since_id, the since_id will be forced to the oldest ID available.
# max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
# include_entities – The entities node will not be included when set to false. Defaults to true.

# details: http://docs.tweepy.org/en/latest/api.html

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
                # 'created_at':tweet.created_at,
               'retweet_count':tweet.retweet_count,
               'favorite_count':tweet.favorite_count,
               'importance_index': importance_index,
               'geo': tweet.geo,
               'coordinates': tweet.coordinates,
               'place':tweet.place
               }

        json.dump(dic, f, indent=2, ensure_ascii=False)
        f.write('\n')
        # time.sleep(30)


# filename = 'retweets_{}.json'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
# with open(filename, 'w', encoding="utf-8") as f:
#     for tweet in tweets:
#         importance_index = round(tweet.retweet_count * 1.0 + tweet.favorite_count * 0.1)
#         dic = {'text': tweet.text,
#                'date': str(tweet.created_at),
#                'id': tweet.id,
#                'user_id':tweet.user.id,
#                 # 'created_at':tweet.created_at,
#                'retweet_count':tweet.retweet_count,
#                'favorite_count':tweet.favorite_count,
#                'importance_index': importance_index
#                }

#         json.dump(dic, f, ensure_ascii=False)
#         f.write('\n')
#         time.sleep(300)