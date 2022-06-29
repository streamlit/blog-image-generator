import streamlit as st
from htbuilder import svg, ellipse

def render():
    data = [None, '', []]

    avatar = st.file_uploader("User/Company logo", help="This image gets displayed at the top-left hand-corner")
    if avatar is not None: data[0] = avatar

    avatar_text = st.text_input('User/Company text', placeholder='Streamlit corp.', help="This text gets displayed at the top-left hand-corner, along with the avatar/logo")
    if avatar_text is not '': data[1] = avatar_text

    images = st.file_uploader("Choose images", help="Recommended size: 710x460 pixels", accept_multiple_files=True)
    if len(images) >= 2: data[2] = images

    return [data]

def generate(data):
    verify_arguments(data)

    return str(
        svg(view_box=(0, 0, 200, 100), xmlns="http://www.w3.org/2000/svg")(
            ellipse(cx=100, cy=50, rx=100, ry=50)
        )
    )
    # Outputs this:
    #
    # """
    # <svg viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
    #   <ellipse cx="100" cy="50" rx="100" ry="50" />
    # </svg>
    # """


def verify_arguments(data):
    MIN_IMAGES = 2

    assert data[0] is not None, "Please add an avatar"
    assert data[1] is not '', "Please add the person/company text"
    assert len(data[2]) >= MIN_IMAGES, "Please choose at least two images"