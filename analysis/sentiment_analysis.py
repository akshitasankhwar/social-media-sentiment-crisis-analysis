
# analysis/sentiment_analysis.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import os

def analyze_sentiments(input_csv="data/tweets_clean.csv", output_csv="data/tweets_sentiment.csv"):
    try:
        nltk.download('vader_lexicon')
        df = pd.read_csv(input_csv)

        sid = SentimentIntensityAnalyzer()

        sentiments = []
        for text in df["Cleaned_Text"]:
            score = sid.polarity_scores(text)
            if score["compound"] >= 0.05:
                sentiments.append("Positive")
            elif score["compound"] <= -0.05:
                sentiments.append("Negative")
            else:
                sentiments.append("Neutral")

        df["Sentiment"] = sentiments
        df["Label"] = df["Sentiment"]
        df.to_csv(output_csv, index=False)
        print(f"✅ Sentiment analysis complete. Output saved to {output_csv}")
    except Exception as e:
        print("❌ Error during sentiment analysis:", e)

if __name__ == "__main__":
    analyze_sentiments()

