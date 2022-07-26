import streamlit as st
import time as time
import streamlit.components.v1 as components


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
          label="Download image",
          data=final_images[i],
          file_name="image.svg",
          mime="image/svg+xml"
        )

        st.write('')
        st.write('')
