# analysis/detect_crisis.py

import pandas as pd
import os

def detect_crisis(input_csv="data/tweets_sentiment.csv", output_csv="data/tweets_crisis.csv"):
    try:
        df = pd.read_csv(input_csv)

        # List of crisis-related keywords
        crisis_keywords = [
            "help", "emergency", "urgent", "need", "stuck", "trapped", "destroyed",
            "dead", "missing", "collapsed", "rescue", "flooded", "earthquake",
            "riot", "panic", "disaster", "evacuate", "fire", "injured"
        ]

        # Function to check if tweet contains any crisis keyword
        def is_crisis(text):
            text_lower = str(text).lower()
            for word in crisis_keywords:
                if word in text_lower:
                    return "Crisis"
            return "Non-Crisis"

        # Apply function to each tweet
        df["Crisis_Label"] = df["Cleaned_Text"].apply(is_crisis)

        # Save updated data
        os.makedirs("data", exist_ok=True)
        df.to_csv(output_csv, index=False)
        print(f"🚨 Crisis detection complete. Output saved to {output_csv}")

    except Exception as e:
        print("❌ Error during crisis detection:", e)

if __name__ == "__main__":
    detect_crisis()
