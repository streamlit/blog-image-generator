import streamlit as st
from . import step2_announcement, step2_community, step2_monthly_rewind, step2_case_study, step2_tutorial, step2_release_notes


STEPS = {
    'Announcement': step2_announcement,
    'Community': step2_community,
    'Monthly rewind': step2_monthly_rewind,
    'Case study': step2_case_study,
    'Tutorial': step2_tutorial,
    'Release notes': step2_release_notes,
}

def step2(selected_template):
    st.write('''
    ## Step 2: Add your assets!
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