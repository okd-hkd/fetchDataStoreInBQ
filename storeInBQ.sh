#!/bin/bash
while true; do 
 today=$(date +"%Y-%m-%d")

 # yesterday = date -v -1d

 python fetch_tweets.py
 gsutil cp *.json gs://okada_strage/tweets/$today/
 
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

 rm *.json
 sleep 3m
done