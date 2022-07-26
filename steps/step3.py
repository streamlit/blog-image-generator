import streamlit as st
import time as time
import streamlit.components.v1 as components


def step3(final_images):
    st.write('''
    ## Step 3: Download
    ''')

    st.success('Done! Here are a couple options for you. Don\'t like the gradients? Hit "Generate" again!')

    for i in range(len(final_images)):
      components.html(final_images[i], height=340)
      st.download_button(
        label="Download image",
        data=final_images[i],
        file_name="image.svg",
        mime="image/svg+xml"
      )