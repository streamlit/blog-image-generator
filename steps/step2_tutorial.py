import streamlit as st
from htbuilder import svg, ellipse

def render():
    images = st.file_uploader("Choose images", help="Recommended size for each image: 610x350 pixels", accept_multiple_files=True)
    return [images]


def generate(images):
    verify_arguments(images)

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


def verify_arguments(images):
    MIN_IMAGES = 2

    assert len(images) >= MIN_IMAGES, "Please choose at least two images"