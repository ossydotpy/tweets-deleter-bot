import os
import json
import time
import tweepy
import concurrent.futures
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.environ.get("API_KEY")
consumer_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

batch_size = 50
tweet_ids = []


def process_tweets():
    with open('tweets.json', encoding='utf-8') as f:
        tweets_data = json.load(f)

    for item in tweets_data:
        tweet_ids.append(item['tweet']['id'])


def delete_tweet(api, tweet_id):
    try:
        api.destroy_status(tweet_id)
        print("T - Deleted: " + tweet_id)
        return True
    except tweepy.errors.TweepyException as e:
        if isinstance(e, tweepy.NotFound):
            print("  D ---Tweet not found / Already deleted: ", tweet_id)
        elif isinstance(e, tweepy.Unauthorized):
            print("  D ---Unauthorized: ", tweet_id)
        elif isinstance(e, tweepy.TooManyRequests):
            print("ERROR: Rate limit reached. Exiting.")
            return False
        else:
            print("ERROR: ---", e, tweet_id)
            return False
    except Exception as e:
        print("ERROR: ---", e, tweet_id)
        return False


def make_threads():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print('''
    >> Deletion of tweets takes a long time due to the sluggish Twitter API. The script uses multithreading to delete 
    threads faster. However, it might still take a few minutes to delete your entire history of tweets if it exceeds 
    a couple of thousand tweets.''')

    # Use ThreadPoolExecutor to manage threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        api = tweepy.API(auth)
        futures = [executor.submit(delete_tweet, api, tweet_id) for tweet_id in tweet_ids]

    print("\n\n--> Process finished in %s seconds." % (time.time() - start_time))


process_tweets()
start_time = time.time()
make_threads()
