import streamlit as st
from slugify import slugify

def step1():
    st.write('''
    ## Step 1: Pick a category

    Select the category of your image, and get a preview of the template we'll use for it.

    ''')

    # Pick type of template
    EMPTY = 'Pick an option!'
    template = st.selectbox(
      'Type of image:',
      (EMPTY, 'Announcement', 'Community', 'Monthly rewind', 'Case study', 'Tutorial', 'Release notes')
    )

    # Show the selected one
    if template == EMPTY:
        return None

    imageUrl = "%s-%s.%s" %('img/template',slugify(template),'jpg')
    imageCaption = "%s %s" %('Template for',template)

    st.write('Great choice! Your image will look like this 👇🏻')
    st.image(imageUrl, caption=imageCaption)

    return template
