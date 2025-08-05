import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_sentiment(csv_path="data/tweets_sentiment.csv"):
    try:
        df = pd.read_csv(csv_path)

        # Check if 'Label' column exists
        if 'Label' not in df.columns:
            print("❌ 'Label' column not found. Please run the sentiment analysis script first.")
            return

        # Count the sentiment labels
        sentiment_counts = df["Label"].value_counts()

        # Plotting
        plt.figure(figsize=(6, 4))
        sentiment_counts.plot(kind='bar')
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Number of Tweets")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("visualization/sentiment_plot.png")
        plt.show()

        print("✅ Sentiment plot saved to 'visualization/sentiment_plot.png'")

    except Exception as e:
        print("❌ Error while plotting sentiment distribution:", e)

if __name__ == "__main__":
    plot_sentiment()

