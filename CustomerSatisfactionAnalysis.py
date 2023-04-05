# to predict fellings
import streamlit as st     

# NLTL - Natural Language Toolkit
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# system title
st.write('Customer Satisfaction Analysis')

# input - customer comment
user_input = st.text_input('Please, rate our services: ')

# predict creation
nltk.download('vader_lexicon')
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input) # this var predict the user sentimental

if score == 0:
    st.write('')
elif score['neg'] != 0:
    st.write('#negative rate')
elif score['pos'] != 0:
    st.write('#positive rate')

