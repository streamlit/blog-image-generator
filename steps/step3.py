import streamlit as st
import time as time

def step3(final_image):
    st.write('''
    ## Step 3: Download
    ''')

    st.success('Done! Preview and download your image below')

    # Temporary code...

    # Trying to show the image preview via HTML, but not working for some reason...
    #st.markdown(final_image, unsafe_allow_html=True)

    # Trying to show using st.image, but that only partially works. Need to debug...
    st.image(final_image)

    st.download_button(
      label="Download image",
      data=final_image,
      file_name="image.svg",
      mime="image/svg+xml"
    )
