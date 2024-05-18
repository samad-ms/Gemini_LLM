from  dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-1.0-pro')
chat=model.start_chat(history=[])

def gemini_response(question):
    respose=chat.send_message(question,stream=True)
    return respose

#initialize streamlit app
st.set_page_config(page_title='Q&A Demo')
st.header('gemini LLM Application')

# initialize sesstion state for chat history if doesnt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input= st.text_input('input:' ,key='input')
submit= st.button('ask question')

if input and submit:
    response=gemini_response(input)
    st.session_state['chat_history'].append(('you',input))
    st.subheader('The Respose is ')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('bot',chunk.text))
st.subheader('The History is ')
for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")