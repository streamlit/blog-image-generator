import streamlit as st
import time as time
import streamlit.components.v1 as components


def step3(final_image):
    st.write('''
    ## Step 3: Download
    ''')

    st.success('Done! Preview and download your image below. Don\'t like the gradient? Hit "Generate" again!')

    components.html(final_image, height=340)

    st.download_button(
      label="Download image",
      data=final_image,
      file_name="image.svg",
      mime="image/svg+xml"
    )
