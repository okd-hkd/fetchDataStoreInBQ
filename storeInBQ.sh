#!/bin/bash
while true; do 
 today=$(date +"%Y-%m-%d")
 python fetch_tweets.py
 gsutil cp *.json gs://okada_strage/tweets/$today/
 
 # load コマンドを実行すると、テーブルにデータが読み込まれる
 bq load --source_format=NEWLINE_DELIMITED_JSON twitter.fetchFromTwitterAPITable gs://okada_strage/tweets/$today/`ls *.json` text:STRING,date:STRING,id:INTEGER,user_id:INTEGER,importance_index:INTEGER,retweet_count:INTEGER,favorite_count:INTEGER
 
 rm *.json
 sleep 5m
done