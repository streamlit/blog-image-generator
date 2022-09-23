import streamlit as st
import time as time
import streamlit.components.v1 as components


def display_output():
    st.write('''
    ## Step 3: Download
    ''')

    svg_images = st.session_state.images

    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(svg_images)):

        components.html(f'''
            <body style="margin: 0; padding: 0;">
                <svg viewBox="0 0 1480 700">{svg_images[i]}</svg>
            </body>
        ''', height=333)

        st.download_button(
            label="Download SVG image",
            data=svg_images[i],
            file_name=f'''{st.session_state.template_name}.svg''',
            mime="image/svg+xml"
        )

        st.write('')
        st.write('')
