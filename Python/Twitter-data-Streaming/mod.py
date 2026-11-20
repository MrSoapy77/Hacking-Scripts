import tweepy
import time
from kafka import KafkaConsumer, KafkaProducer
import os
# Credentials come from environment variables so they are never committed.
consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
from datetime import datetime
def normalize_timestamp(time):
  mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
  return(mytime.strftime("%Y-%m-%d %H:%M:%S"))
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(2,0,2))
topic_name = 'dhruv2612'
def get_twitter_data():
  # tweepy 4 renamed API.search to API.search_tweets
  res = api.search_tweets("BCCI")
  for i in res:
    record = ''
    record += str(i.user.id_str)
    record += '\n'
    record += str(i.text)
    record += ';\n'
    record += str(normalize_timestamp(str(i.created_at)))
    record += ';' 
    record += str(i.user.followers_count)
    record += ';'
    record += str(i.user.location)
    record += ';'
    record += str(i.favorite_count)
    record += ';'
    record += str(i.retweet_count)
    record += ';'
    producer.send(topic_name, str.encode(record))
get_twitter_data()

def periodic_work(interval):
  while True:
    get_twitter_data()
    time.sleep(interval)

periodic_work(60*0.1) 
