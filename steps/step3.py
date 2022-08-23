import streamlit as st
import time as time
import streamlit.components.v1 as components
from cairosvg import svg2png

def download_png(image):
    png_image = svg2png(bytestring=image,output_width=1480, output_height=700)

    st.write('Good choice! The SVG should already be in your downloads folder.')

    st.info('Need the PNG file as well? Download below!')

    st.download_button(
        label="Download PNG image",
        data=png_image,
        file_name="image.png",
        mime="image/png",
        key="png_image"
    )
    

def step3(final_images):
    st.write('''
    ## Step 3: Download
    ''')

    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(final_images)):

        components.html(f'''
            <body style="margin: 0; padding: 0;">
                {final_images[i]}
            </body>
        ''', height=340)

        st.download_button(
            label="Download this image",
            data=final_images[i],
            file_name="image.svg",
            mime="image/svg+xml",
            on_click=download_png,
            args=[final_images[i]],
            key=f"final_image_{i}"
        )

        st.write('')
        st.write('')
