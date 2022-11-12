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

import streamlit as st
import time as time
import streamlit.components.v1 as components
from cairosvg import svg2png

@st.cache
def to_png(svg_image):
    return svg2png(bytestring=svg_image, output_width=1480, output_height=700)

def step3(svg_images):
    st.write('''
    ## Step 3: Download
    ''')

    st.info("Done! We've generated some options for you 👇🏻")

    for i in range(len(svg_images)):

        components.html(f'''
            <body style="margin: 0; padding: 0;">
                {svg_images[i]}
            </body>
        ''', height=340)

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
