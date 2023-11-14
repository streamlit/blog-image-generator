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
import random
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
            mime="image/svg+xml",
            key= f"key_{str(random.randint(0, 100000000))}"
        )

        st.write('')
        st.write('')
