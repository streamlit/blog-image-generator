import streamlit as st
import time as time
import streamlit.components.v1 as components
#from cairosvg import svg2png

@st.cache
def to_png(svg_image):
    return svg_image #svg2png(bytestring=svg_image, output_width=1480, output_height=700)


def display_output():
    st.write('''
    ## Step 3: Download
    ''')

    svg_images = st.session_state.images

    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(svg_images)):

        components.html(f'''
            <body style="margin: 0; padding: 0;">
                {svg_images[i]}
            </body>
        ''', height=333)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download SVG image",
                data=svg_images[i],
                file_name="image.svg",
                mime="image/svg+xml"
            )

        with col2:
            png_image = to_png(svg_images[i])
            st.download_button(
                label="Download PNG image",
                data=png_image,
                file_name="image.png",
                mime="image/png"
            )

        st.write('')
        st.write('')
