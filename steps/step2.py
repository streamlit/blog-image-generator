import streamlit as st
from . import step2_announcement


STEPS = {
    'Announcement': step2_announcement,
}

def step2(selected_template):
    st.write('''
    ## Step 2: Add your assets!

    Add the images required for this template to work as expected
    ''')

    # Show an error message if no template was selected
    if selected_template not in STEPS:
        st.error('No template selected! Please, go back to the previous page and pick one first.')
        return

    st.write("Nice! Let's add the necessary assets for the", selected_template, 'template:')

    curr_step = STEPS[selected_template]

    with st.form(key="step2_form"):
        user_arguments = curr_step.render()

        if st.form_submit_button("Generate"):
            final_image = curr_step.generate(*user_arguments)
            return final_image

    return None

# OLD
#         # Show the relevant inputs for each type of template
#         if selected_template == 'Announcement'):
#             image = st.file_uploader("Choose an image", help="Recommended size: 1290x520 pixels")
#         elif (selected_template == 'Community' or selected_template == 'Tutorial'):
#             images = st.file_uploader("Choose images", help="Recommended size: 610x350 pixels", accept_multiple_files=True)
#         elif (selected_template == 'Monthly rewind'):
#             col1, col2, col3, col4 = st.columns(4)
#             with col1:
#                 emoji_1 = st.text_input('Emoji 1', '', placeholder='👻')
#             with col2:
#                 emoji_2 = st.text_input('Emoji 2', '', placeholder='🤖')
#             with col3:
#                 emoji_3 = st.text_input('Emoji 3', '', placeholder='🍘')
#             with col4:
#                 emoji_4 = st.text_input('Emoji 4', '', placeholder='🐍', help="You can add up to 4. Leave them empty if you want to have less than 4!")
#         elif (selected_template == 'Case study'):
#             avatar = st.file_uploader("User/Company logo", help="This image gets displayed at the top-left hand-corner")
#             avatar_text = st.text_input('User/Company text', '', placeholder='Streamlit corp.', help="This text gets displayed at the top-left hand-corner, along with the avatar/logo")
#             images = st.file_uploader("Choose images", help="Recommended size: 710x460 pixels", accept_multiple_files=True)
#         elif (selected_template == 'Release notes'):
#             col1, col2 = st.columns(2)
#             with col1:
#                 emoji = st.text_input('Emoji', '', placeholder='🚢', help="If you leave it empty, we'll default it to :rocket:")
#             with col2:
#                 emoji_2 = st.text_input('Version number', '', placeholder='v.1.10.0', help="This text shows up at the bottom-right hand-corner")

#         # Store it on state
#         st.button('Generate the image!')
