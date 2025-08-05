# analysis/fetch_tweets.py

import tweepy
import pandas as pd
import os
import sys

# Add parent directory to sys.path to import config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import BEARER_TOKEN

def fetch_tweets(keyword="flood", max_results=20):
    try:
        # Connect to Twitter API v2 using Bearer Token
        client = tweepy.Client(bearer_token=BEARER_TOKEN)

        # Fetch tweets
        response = client.search_recent_tweets(
            query=keyword,
            max_results=max_results,
            tweet_fields=["id", "created_at", "text", "author_id", "lang"]
        )

        tweets = response.data
        tweet_data = []

        if tweets:
            for tweet in tweets:
                tweet_data.append([
                    tweet.id,
                    tweet.created_at,
                    tweet.author_id,
                    tweet.text.replace('\n', ' ')
                ])
            # Save to CSV
            os.makedirs("data", exist_ok=True)
            df = pd.DataFrame(tweet_data, columns=["ID", "Timestamp", "User", "Text"])
            df.to_csv("data/tweets_raw.csv", index=False)
            print(f"✅ {len(df)} tweets saved to data/tweets_raw.csv")
        else:
            print("⚠️ No tweets found.")

    except Exception as e:
        print("❌ Error fetching tweets:", e)

if __name__ == "__main__":
    fetch_tweets("flood", max_results=50)
