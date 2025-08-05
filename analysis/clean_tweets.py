# analysis/clean_tweets.py

import pandas as pd
import re
import os

def clean_text(text):
    # Remove mentions (@user)
    text = re.sub(r'@\w+', '', text)

    # Remove hashtags (#tag)
    text = re.sub(r'#\w+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Remove emojis and non-alphanumeric characters
    text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def clean_tweet_data(input_csv="data/tweets_raw.csv", output_csv="data/tweets_clean.csv"):
    try:
        df = pd.read_csv(input_csv)
        df["Cleaned_Text"] = df["Text"].apply(clean_text)
        df.to_csv(output_csv, index=False)
        print(f"✅ Cleaned tweets saved to {output_csv}")
    except Exception as e:
        print("❌ Error cleaning tweets:", e)

if __name__ == "__main__":
    clean_tweet_data()
