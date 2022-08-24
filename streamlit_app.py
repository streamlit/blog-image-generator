import streamlit as st
from slugify import slugify
from steps import step1
from steps import step2
from steps import step3

# Presentational content

st.markdown('<div style="font-size: 4rem; margin-bottom: -3rem;">🎨</div>', unsafe_allow_html=True)

'''
# Blog image generator

An app to generate good-looking images for [our blog](https://blog.streamlit.io).
'''

'---'

step1.display_form()

if step1.is_form_complete():
    ''
    ''
    step2.display_form()
else:
    step2.reset()
    st.stop()

if step2.is_form_complete():
    ''
    ''
    step3.display_output()
