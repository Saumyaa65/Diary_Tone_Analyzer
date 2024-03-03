import streamlit as st
import plotly.express as px
import glob
import nltk
import re

nltk.download("vader_lexicon")
from nltk.sentiment import SentimentIntensityAnalyzer
analyzer=SentimentIntensityAnalyzer()

st.header("Diary Tone")
st.subheader("Positivity")

filepaths=glob.glob("diary/*.txt")

positivity=[]
negativity=[]
dates=[]

for filepath in filepaths:
    with open(filepath, 'r') as file:
        content=file.read()

    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

    pattern=re.compile("[0-9]+")
    finding=re.findall(pattern, filepath)
    date= "Oct "+finding[2]
    dates.append(date)

figure= px.line(x=dates, y=positivity,
                labels={'x': "Date", 'y': "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure= px.line(x=dates, y=negativity,
                labels={'x': "Date", 'y': "Negativity"})
st.plotly_chart(figure)