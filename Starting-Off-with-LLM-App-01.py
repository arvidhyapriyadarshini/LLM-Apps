from dotenv import load_dotenv
load_dotenv() #load environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#load geminipro model and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])
    return response.text


#Initialize the Streamlit app

st.set_page_config(page_title="LLM & LIM Projects")
st.header("Gemini-pro-vision LLM & LIM Application")
input =st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell about the image")

if submit:
    response=get_gemini_response(input, image)
    st.subheader("the response is:")
    st.write(response)




