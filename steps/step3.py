import streamlit as st
import time as time

def step3(final_image):
    st.write('''
    ## Step 3: Download
    ''')

    st.success('Done! Preview and download your image below')
    st.markdown(final_image, unsafe_allow_html=True)

    st.download_button(
      label="Download image",
      data=final_image,
      file_name="image.svg",
      mime="image/svg+xml"
    )
