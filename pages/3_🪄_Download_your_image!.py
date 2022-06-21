import streamlit as st
import time as time

with st.spinner('Generating your image...'):
  time.sleep(5)
st.success('Done! Preview and download your image below 👇🏻')
st.image('img/example.jpg', caption='This is your generated image')
with open("img/example.jpg", "rb") as file:
  st.download_button(
    label="Download image",
    data=file,
    file_name="image.jpg",
    mime="image/jpg"
  )