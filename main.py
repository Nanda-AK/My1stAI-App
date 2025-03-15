from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']


### My Python Code to generate Tweet 
# Generate using Prompt Template

tweet_template ="""
'Give me {number} tweets on Topic {topic}'
give me 5 hashtag per tweet along with popularity counter e.g. #NatureLover(97456)

Use below format as e.g
Tweet sample 1:
This is Great New, he looks awsome in this photo.

Tweet sample 2:
This is crazy, i can not belive this has happned to him.
"""

tweet_prompt = PromptTemplate(template = tweet_template, input_variables =['number','topic'])

#Initializing the Google Gemini Model Flatsh 1.5
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#Create LLM Chain using theprompt template and Model
tweet_chain = tweet_prompt | gemini_model

#Example of using the LLM Chain
#response = tweet_chain.invoke({"number": 5, "topic": "Nature is my God"})

#print(f"\n\n\nBelow is the sampel tweet from LLM\n\n\n {response.content}")

### Below code on streamlit ####
import streamlit as st

st.header("🐦 Tweet Generator")

st.subheader("Generate tweets using Generative AI 🤖")

topic = st.text_input("Topic for tweet :")

number = st.number_input("Enter a Number of tweets 1 to 10 :", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"topic" : topic})
    st.write(tweets.content)
    
