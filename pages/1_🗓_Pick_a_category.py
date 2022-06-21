import streamlit as st
from slugify import slugify

'''
# Step 1: Pick a category

Select the category of your image, and get a preview of the template we'll use for it.

----
'''

# Initialize state to keep track of steps
if 'selected_template' not in st.session_state:
  st.session_state['selected_template'] = ''

# Function to store the template in state
def store_template():
  st.session_state['selected_template'] = template

# Pick type of template
empty = 'Pick an option!'
template = st.selectbox(
  'Type of image:',
  (empty, 'Announcement', 'Community', 'Monthly rewind', 'Case study', 'Tutorial', 'Release notes')
)

# Show the selected one
if template != empty:
  imageUrl = "%s-%s.%s" %('img/template',slugify(template),'jpg')
  imageCaption = "%s %s" %('Template for',template)

  st.write('Great choice! Your image will look like this 👇🏻')
  st.image(imageUrl, caption=imageCaption)

  # Store it on state
  st.button('Select this template ✔️', on_click=store_template)