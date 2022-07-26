import streamlit as st
from slugify import slugify

TEMPLATES = ('Announcement', 'Community', 'Monthly rewind', 'Case study', 'Tutorial', 'Release notes')

def step1():
    st.write('''
    ## Step 1: Pick a category

    Select the category of your image, and get a preview of the template we'll use for it.
    ''')

    # Pick type of template
    EMPTY = 'Pick an option!'

    a, b, c = st.columns(3)

    if 'template_id' not in st.session_state or st.session_state.template_id is None:
        with a:
            thumbnail(0)
            st.write("")
            thumbnail(1)

        with b:
            thumbnail(2)
            st.write("")
            thumbnail(3)

        with c:
            thumbnail(4)
            st.write("")
            thumbnail(5)

    else:
        st.write(f'#### You selected: { TEMPLATES[st.session_state.template_id] }')
        show_image(st.session_state.template_id, large_caption=False)

        st.button('Pick another template', on_click=set_template, args=[None])

        template = TEMPLATES[st.session_state.template_id]
        return template


def set_template(i):
    st.session_state.template_id = i

def thumbnail(i):
    show_image(i, large_caption=True)

    if 'template_id' in st.session_state and st.session_state.template_id == i:
        st.button('Selected!', disabled=True, key=f"template-{i}")

    else:
        st.button("Select this", key=f"template-{i}", on_click=set_template, args=[i])

def show_image(i, large_caption):
    image_name = TEMPLATES[i]

    if large_caption:
        st.write(f"**{image_name}**")

    image_url = "%s-%s.%s" %('img/template',slugify(image_name),'jpg')

    st.image(image_url)
