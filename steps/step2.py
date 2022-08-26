import streamlit as st
from . import step2_announcement, step2_community, step2_monthly_rewind, step2_case_study, step2_tutorial, step2_release_notes


TEMPLATE_TYPES = {
    'Announcement': step2_announcement,
    'Community': step2_community,
    'Monthly rewind': step2_monthly_rewind,
    'Case study': step2_case_study,
    'Tutorial': step2_tutorial,
    'Release notes': step2_release_notes,
}


def display_form():
    st.write('''
    ## Step 2: Add your assets!

    Customize the selected template with your own assets.
    ''')

    selected_template = st.session_state.template_name

    # Show an error message if no template was selected
    if selected_template not in TEMPLATE_TYPES:
        st.error('No template selected! Please, go back to the previous page and pick one first.')
        return

    st.write("Nice! Let's add the necessary assets for the", selected_template, 'template:')

    curr_step = TEMPLATE_TYPES[selected_template]

    with st.form(key="step2_form"):
        user_arguments = curr_step.render()

        if st.form_submit_button("Generate"):
            st.session_state.images = curr_step.generate(*user_arguments)


def reset():
    if is_form_complete():
        del st.session_state.images


def is_form_complete():
    return 'images' in st.session_state
