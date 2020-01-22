# coding=utf-8
from dotenv import load_dotenv, find_dotenv
import os
import math
import time

from json import JSONEncoder
class MyEncoder(JSONEncoder):
        def default(self, o):
            print(o)
            return o.__dict__  

def json_serial(obj):
    # ??????????????
    if isinstance(obj, (datetime)):
        return obj.isoformat()
    # ????????????.
    raise TypeError ("Type %s not serializable" % type(obj))

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

# トレンド取得可能な地域のwoeidを取得

trends_availabale = api.trends_available()
trends_location_codes_list = []
for i in trends_availabale :
  if i['country'] == 'Japan':
    trends_location_codes_list.append(i['woeid'])


import json
from datetime import datetime

# Write tweets to json file.
filename = '/trends_{}.json'.format(datetime.now().strftime('%Y%m%d%H%M%S'))
with open('trends/'+ filename, 'w', encoding="utf-8") as f:
  for location_code in trends_location_codes_list: 
      
      trend_of_a_specific_location = api.trends_place(location_code )
      # importance_index = round(tweet.retweet_count * 1.0 + tweet.favorite_count * 0.1)
      for index in range(len(trend_of_a_specific_location[0]['trends'])):
        rank = str(index) +'/'+ str(len(trend_of_a_specific_location[0]['trends']))
        dic = { 
            'as_of':trend_of_a_specific_location[0]['as_of'],
            'created_at': trend_of_a_specific_location[0]['created_at'],
            'location_name':trend_of_a_specific_location[0]['locations'][0]['name'],
            'location_code':trend_of_a_specific_location[0]['locations'][0]['woeid'],
            'name': trend_of_a_specific_location[0]['trends'][index]['name'],
            "url": trend_of_a_specific_location[0]['trends'][index]['name'],
            "promoted_content": trend_of_a_specific_location[0]['trends'][index]['promoted_content'],
            "query": trend_of_a_specific_location[0]['trends'][index]['query'],
            "tweet_volume": trend_of_a_specific_location[0]['trends'][index]['tweet_volume'],
            'rank':index,
          }
        # dic.update(dic)
        # print(dic)      
        json.dump(dic, f, ensure_ascii=False,cls=MyEncoder,default=json_serial)
        f.write('\n')
time.sleep(180) 
