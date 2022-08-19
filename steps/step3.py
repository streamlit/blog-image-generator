import streamlit as st
import time as time
import streamlit.components.v1 as components
from cairosvg import svg2png
from PIL import Image
import io

def download_png(image):
    png_image = svg2png(bytestring=image,output_width=1480, output_height=700, write_to="./img/temp/image.png")

    with open('./img/temp/image.png', 'rb') as image:
        img_data = image.read()
        im = Image.open(io.BytesIO(img_data))
        im.show()

def step3(final_images):
    st.write('''
    ## Step 3: Download

    Done! We've generated a few options for you.
    ''')

    st.warning('Don\'t like the gradients below? Hit "Generate" again!')

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
            args=[final_images[i]]
        )

        st.write('')
        st.write('')
