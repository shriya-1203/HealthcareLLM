# build a groq chat app using streamlit and groqAPI, and use dotenv to hide api keys 

import streamlit as st
from groq import Groq   
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

#create a client
client = Groq(api_key=groq_api_key)

#set page title
st.set_page_config(page_title="Healthcare LLM")

#set page header
st.title("Healthcare LLM")

#set page subheader
st.subheader("A healthcare LLM specialized in repsonding to health related quaeries")

#set page description
st.write("Healthcare LLM is specialized in repsonding to health related quaeries")


#set system prompt
system_prompt = {
    "role": "system",
    "content": "You are a healthcare LLM specialized in repsonding to health related quaeries"
}

#initialize chat history
chat_history = [system_prompt]

#initialize user input
user_input = st.text_input("Enter your query:")

#add user input to chat history
chat_history.append({"role": "user", "content": user_input})

response = client.chat.completions.create(model="llama3-70b-8192", messages=chat_history)

chat_history.append({"role": "assistant", "content": response.choices[0].message.content})

#print response
st.write(response.choices[0].message.content)

# streamlit run main.py

