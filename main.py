# main.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set Streamlit page settings
st.set_page_config(page_title="Social Media Sentiment & Crisis Dashboard", layout="centered")

# Title
st.title("📊 Social Media Sentiment & Crisis Analysis")

# Load Data
try:
    df = pd.read_csv("data/tweets_crisis.csv")
except FileNotFoundError:
    st.error("CSV file not found. Please run the analysis scripts first.")
    st.stop()

# Section 1: Sentiment Distribution
st.header("🧠 Sentiment Distribution")
sentiment_counts = df["Sentiment"].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
ax1.axis('equal')
st.pyplot(fig1)

# Section 2: Crisis Detection
st.header("🚨 Crisis vs Non-Crisis Tweets")
crisis_counts = df["Crisis_Label"].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(crisis_counts, labels=crisis_counts.index, autopct='%1.1f%%', startangle=140)
ax2.axis('equal')
st.pyplot(fig2)

# Section 3: Filtered Tweet Table
st.header("🔍 View Tweets by Filters")

sentiment_option = st.selectbox("Choose Sentiment:", ["All"] + list(sentiment_counts.index))
crisis_option = st.selectbox("Choose Crisis Label:", ["All"] + list(crisis_counts.index))

filtered_df = df.copy()
if sentiment_option != "All":
    filtered_df = filtered_df[filtered_df["Sentiment"] == sentiment_option]
if crisis_option != "All":
    filtered_df = filtered_df[filtered_df["Crisis_Label"] == crisis_option]

st.dataframe(filtered_df[["Timestamp", "User", "Text", "Sentiment", "Crisis_Label"]].reset_index(drop=True))
