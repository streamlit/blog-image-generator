import streamlit as st
from slugify import slugify
from .step2 import TEMPLATE_TYPES

def display_form():
    st.write('''
    ## Step 1: Pick a category

    Select the category of your image, and get a preview of the template we'll use for it.
    ''')

    # Pick type of template
    EMPTY = 'Pick an option!'

    cols = st.columns(3)

    if 'template_name' not in st.session_state:
        for i, template_name in enumerate(TEMPLATE_TYPES.keys()):
            with cols[i % len(cols)]:
                display_thumbnail(template_name)

    else:
        st.write(f'#### You selected: { st.session_state.template_name }')
        display_image(st.session_state.template_name)

        st.button(
            'Pick another template',
            on_click=reset)


def is_form_complete():
    return 'template_name' in st.session_state


def reset():
    if 'template_name' in st.session_state:
        del st.session_state.template_name


def set_template(template_name):
    st.session_state.template_name = template_name


def display_thumbnail(template_name):
    st.write(f"**{template_name}**")

    display_image(template_name)

    st.button(
        "Select this",
        key=f"template-{template_name}",
        on_click=set_template,
        args=[template_name])

    st.write("")
    st.write("")


def display_image(template_name):
    image_url = "%s-%s.%s" % ('img/template', slugify(template_name),'jpg')
    st.image(image_url)
