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

TEMPLATES = ('Announcement', 'Community', 'Monthly rewind', 'Case study', 'Tutorial', 'Release notes')

def step1(on_template_changed):
    st.write('''
    ## Step 1: Pick a category

    Select the category of your image, and get a preview of the template we'll use for it.
    ''')

    # Pick type of template
    EMPTY = 'Pick an option!'

    a, b, c = st.columns(3)

    if 'template_id' not in st.session_state or st.session_state.template_id is None:
        with a:
            thumbnail(0, on_template_changed)
            st.write("")
            thumbnail(1, on_template_changed)

        with b:
            thumbnail(2, on_template_changed)
            st.write("")
            thumbnail(3, on_template_changed)

        with c:
            thumbnail(4, on_template_changed)
            st.write("")
            thumbnail(5, on_template_changed)

    else:
        st.write(f'#### You selected: { TEMPLATES[st.session_state.template_id] }')
        show_image(st.session_state.template_id, large_caption=False)

        st.button(
            'Pick another template',
            on_click=set_template,
            args=[None, on_template_changed])

        template = TEMPLATES[st.session_state.template_id]

        return template


def set_template(i, on_template_changed):
    st.session_state.template_id = i
    on_template_changed()


def thumbnail(i, on_template_changed):
    show_image(i, large_caption=True)

    if 'template_id' in st.session_state and st.session_state.template_id == i:
        st.button('Selected!', disabled=True, key=f"template-{i}")

    else:
        st.button(
            "Select this",
            key=f"template-{i}",
            on_click=set_template,
            args=[i, on_template_changed])


def show_image(i, large_caption):
    image_name = TEMPLATES[i]

    if large_caption:
        st.write(f"**{image_name}**")

    image_url = "%s-%s.%s" % ('img/template', clean_name(image_name),'jpg')

    st.image(image_url)


def clean_name(name):
    name = name.lower()
    name = name.replace(' ', '-')
    return name
