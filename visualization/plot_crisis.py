# visualization/plot_crisis.py

import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_crisis_distribution(input_csv="data/tweets_crisis.csv"):
    try:
        # Read CSV
        df = pd.read_csv(input_csv)

        # Count Crisis vs Non-Crisis
        crisis_counts = df["Crisis_Label"].value_counts()

        # Plot pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(
            crisis_counts,
            labels=crisis_counts.index,
            autopct='%1.1f%%',
            startangle=140,
            shadow=True
        )
        plt.title("Crisis vs Non-Crisis Tweets")
        plt.tight_layout()

        # Save plot
        os.makedirs("visualization", exist_ok=True)
        plt.savefig("visualization/crisis_pie_chart.png")
        plt.show()

        print("📊 Crisis pie chart saved to visualization/crisis_pie_chart.png")

    except Exception as e:
        print("❌ Error generating crisis plot:", e)

if __name__ == "__main__":
    plot_crisis_distribution()
