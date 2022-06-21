import streamlit as st

'''
# Step 2: Add your assets!

Add the images required for this template to work as expected

----
'''

selected_template = st.session_state['selected_template']

# Show an error message if no template was selected
if(selected_template == ''):
  st.error('No template selected! Please, go back to the previous page and pick one first.')
else:
  template_string = "%s %s %s" %("Nice! Let's add the necessary assets for the",selected_template,'template:')
  st.write(template_string)

  # Show the relevant inputs for each type of template
  if(selected_template == 'Announcement'):
    image = st.file_uploader("Choose an image", help="Recommended size: 1290x520 pixels")
  elif (selected_template == 'Community' or selected_template == 'Tutorial'):
    images = st.file_uploader("Choose images", help="Recommended size: 610x350 pixels", accept_multiple_files=True)
  elif (selected_template == 'Monthly rewind'):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
      emoji_1 = st.text_input('Emoji 1', '', placeholder='👻')
    with col2:
      emoji_2 = st.text_input('Emoji 2', '', placeholder='🤖')
    with col3:
      emoji_3 = st.text_input('Emoji 3', '', placeholder='🍘')
    with col4:
      emoji_4 = st.text_input('Emoji 4', '', placeholder='🐍', help="You can add up to 4. Leave them empty if you want to have less than 4!")
  elif (selected_template == 'Case study'):
    avatar = st.file_uploader("User/Company logo", help="This image gets displayed at the top-left hand-corner")
    avatar_text = st.text_input('User/Company text', '', placeholder='Streamlit corp.', help="This text gets displayed at the top-left hand-corner, along with the avatar/logo")
    images = st.file_uploader("Choose images", help="Recommended size: 710x460 pixels", accept_multiple_files=True)
  elif (selected_template == 'Release notes'):
    col1, col2 = st.columns(2)
    with col1:
      emoji = st.text_input('Emoji', '', placeholder='🚢', help="If you leave it empty, we'll default it to :rocket:")
    with col2:
      emoji_2 = st.text_input('Version number', '', placeholder='v.1.10.0', help="This text shows up at the bottom-right hand-corner")

  # Store it on state
  st.button('Generate the image!')