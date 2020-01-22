#!/bin/bash
while true; do 
 today=$(date +"%Y-%m-%d")

 # yesterday = date -v -1d

 python fetch_tweets.py
 python fetch_trends.py
 gsutil cp search_tweets/*.json gs://okada_strage/tweets/$today/
 gsutil cp trends/*.json gs://okada_strage/trends/$today/
 
 # load コマンドを実行すると、テーブルにデータが読み込まれる
 bq load --source_format=NEWLINE_DELIMITED_JSON twitter.fetchFromTwitterAPITable \
 gs://okada_strage/tweets/$today/`ls *.json` \
 text:STRING,status_id:INTEGER,\
user_name:STRING,\
screen_name:STRING,\
tweet_url:STRING,\
location:STRING,\
source:STRING,\
date:STRING,\
date_datetime:DATETIME,\
id:INTEGER,\
user_id:INTEGER,\
profile_image:STRING,\
followers_count:INTEGER,\
importance_index:INTEGER,\
retweet_count:INTEGER,\
favorite_count:INTEGER,\
geo_enabled:BOOLEAN,\
geo_str:STRING,\
coordinates:STRING



 rm search_tweets/*.json
 

  bq load --source_format=NEWLINE_DELIMITED_JSON twitter.trends \
 gs://okada_strage/trends/$today/`ls *.json` \
 as_of:DATETIME,\
created_at:DATETIME,\
location_name:STRING,\
location_code:INTEGER,\
name:STRING,\
url:STRING,\
promoted_content:STRING,\
query:STRING,\
tweet_volume:INTEGER,\
rank:INTEGER

 rm trends/*.json
#  sleep 3m
done