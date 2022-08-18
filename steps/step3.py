import streamlit as st
import time as time
import streamlit.components.v1 as components
from cairosvg import svg2png

def step3(final_images):
    st.write('''
    ## Step 3: Download

    Done! We've generated a few options for you.
    ''')

    st.warning('Don\'t like the gradients below? Hit "Generate" again!')

    png_images = []
    for i in range(len(final_images)):
        
        png_images.append(svg2png(bytestring=final_images[i],output_width=1480, output_height=700))

        components.html(f'''
            <body style="margin: 0; padding: 0;">
                {final_images[i]}
            </body>
        ''', height=340)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                label="Download SVG image",
                data=final_images[i],
                file_name="image.svg",
                mime="image/svg+xml"
            )
        
        with col2:
            st.download_button(
                label="Download PNG image",
                data=png_images[i],
                file_name="image.png",
                mime="image/png"
            )

        st.write('')
        st.write('')
