# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import time as time
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

import cairosvg
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


def convert_svg_to_png(svg_content, output=None):
    if output:
        cairosvg.svg2png(bytestring=svg_content, write_to=output)
    else:
        return cairosvg.svg2png(bytestring=svg_content)


def convert_svg_to_webp(svg_data, output=None):
    png_img = Image.open(BytesIO(convert_svg_to_png(svg_data))).convert("RGBA")
    webp_output = BytesIO()
    png_img.save(webp_output, "WEBP")
    png_img.close()
    return webp_output.getvalue()


@st.cache_data
def generate_image_formats(first_image):
    svg_images = st.session_state['images']
    png_images, webp_images = [], []

    def process_image(svg_image):
        png_image = convert_svg_to_png(svg_image)
        webp_image = convert_svg_to_webp(svg_image)
        return png_image, webp_image

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_image, svg_images))
    
    for png_image, webp_image in results:
        png_images.append(png_image)
        webp_images.append(webp_image)
    
    return svg_images, png_images, webp_images

    
def display_output():
    st.write('''
    ## Step 3: Downloads
    ''')

    svg_images, png_images, webp_images = generate_image_formats(st.session_state['images'][0])
    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(svg_images)):
        
        components.html(f'''
            <body style="margin: 0; padding: 0;">
                <svg viewBox="0 0 1480 700">{svg_images[i]}</svg>
            </body>
        ''', height=333)

        col = st.columns(3)

        with col[0]:
            st.download_button(
                label=f":material/download: SVG ({len(svg_images[i])/1024:.2f} KB)",
                data=svg_images[i],
                file_name=f'''{st.session_state.template_name}.svg''',
                mime="image/svg+xml",
                key= f"key_{str(random.randint(0, 100000000))}"
            )

        with col[1]:
            st.download_button(
                label=f":material/download: PNG ({len(png_images[i])/1024:.2f} KB)",
                data=png_images[i],
                file_name=f'''{st.session_state.template_name}.png''',
                mime="image/png",
                key= f"key_{str(random.randint(0, 100000000))}"
            )
        
        with col[2]:
            st.download_button(
                label=f":material/download: WebP ({len(webp_images[i])/1024:.2f} KB)",
                data=webp_images[i],
                file_name=f'''{st.session_state.template_name}.webp''',
                mime="image/webp",
                key= f"key_{str(random.randint(0, 100000000))}"
            )

        st.write('')
        st.write('')