import streamlit as st
from htbuilder import svg, ellipse

def render():
    image = st.file_uploader("Choose an image", help="Recommended size: 1290x520 pixels")
    return [image]


def generate(image):
    verify_arguments(image)

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


def verify_arguments(image):
    assert image != None, "Please choose an image above"
