from dotenv import load_dotenv,find_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(prompt):
    model=genai.GenerativeModel(model_name="gemini-1.0-pro")
    response=model.generate_content(prompt)
    return response.text

st.set_page_config(page_title='QA')
st.header("Gemini QA")
input=st.text_input("input: ",key='input')
submit=st.button('Ask Question')

if submit:
    response=get_gemini_response(input)
    st.subheader('The Response is : ')
    st.write(response)

