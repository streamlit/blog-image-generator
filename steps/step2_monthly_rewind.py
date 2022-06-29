import streamlit as st
from htbuilder import svg, ellipse

def render():
    col1, col2, col3, col4 = st.columns(4)
    emojis = []
    
    # TODO: Render columns conditionally
    with col1:
        emoji1 = st.text_input('Emoji 1', placeholder='👻')
        if emoji1 is not '': emojis.append(emoji1)
    with col2:
        emoji2 = st.text_input('Emoji 2', placeholder='🤖')
        if emoji2 is not '': emojis.append(emoji2)
    with col3:
        emoji3 = st.text_input('Emoji 3', placeholder='🍘')
        if emoji3 is not '': emojis.append(emoji3)
    with col4:
        emoji4 = st.text_input('Emoji 4', placeholder='🐍', help="You can add up to 4. Leave them empty if you want to have less than 4!")
        if emoji4 is not '': emojis.append(emoji4)
    
    return [emojis]


def generate(emojis):
    verify_arguments(emojis)

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


def verify_arguments(emojis):
    # TODO: Check if the text is actually an emoji
    
    MIN_EMOJIS = 1
    
    assert len(emojis) >= MIN_EMOJIS, "Please add at least one emoji"