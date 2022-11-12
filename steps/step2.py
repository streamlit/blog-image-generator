# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    if 'images' not in st.session_state:
        st.session_state.images = None

    st.write('''
    ## Step 2: Add your assets!

    Customize the selected template with your own assets.
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
            st.session_state.images = curr_step.generate(*user_arguments)

    return st.session_state.images
