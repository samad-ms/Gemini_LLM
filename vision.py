from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

model=genai.GenerativeModel(model_name='gemini-pro-vision')
def get_gemini_respose(input,img):
    if input!='':
        respose=model.generate_content([input,img])
    else:
        respose=model.generate_content(img)
    return respose.text        

st.set_page_config(page_title='QA on image')
st.header('Gemini with image ')

input=st.text_input('input prompt: ',key='input')
uploaded_file=st.file_uploader('choose an image...',type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='uploaded image',use_column_width=True)

submit=st.button('give me respose')

if submit:
    response=get_gemini_respose(input,image)
    st.subheader('Repose: ')
    st.write(response)

