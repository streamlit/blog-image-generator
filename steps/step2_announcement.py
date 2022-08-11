import streamlit as st
from .lib.generate_images import generate_gradient, generate_base64_image, resize_image
from PIL import Image
import io

def render():
    image = st.file_uploader("Choose an image", help="Recommended size: 1300x520 pixels")
    return [image]


def generate(image):
    verify_arguments(image)
    
    # Get image byte data, resize and generate the base64 encoded version
    buffered = resize_image(image, 1290, 520)
    image = generate_base64_image(buffered.getvalue())

    # Generate four different images
    generated_images = []
    for i in range(4):
        gradient = generate_gradient()
        
        generated_images.append(f"""
            <svg width="1480" height="700" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                # Gradient
                <rect width="1480" height="700" fill="url(#gradient)"/>

                # Image path
                <image id="screenshot" x="95" y="180" width="1290" height="520" xlink:href="data:image/jpeg;charset=utf-8;base64,{image}" />

                # White Background
                <path xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd" d="M76 64C69.3726 64 64 69.3726 64 76V700H96V188C96 183.582 99.5817 180 104 180H1376C1380.42 180 1384 183.582 1384 188V700H1416V76C1416 69.3726 1410.63 64 1404 64H76Z" fill="white"/>

                # Circles
                <circle cx="106" cy="122" r="10" fill="#FF6C6C"/>
                <circle cx="146.8" cy="122" r="10" fill="#FFE312"/>
                <circle cx="187.6" cy="122" r="10" fill="#3DD56D"/>

                # Definitions
                <defs>
                    
                    # Image
                    <pattern id="pattern0" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot" x="0" y="0" width="1290" height="520" xlink:href="data:image/jpeg;charset=utf-8;base64,{image}" />
                    </pattern>

                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0">{gradient}</linearGradient>
                </defs>
            </svg>
        """.strip())

    return generated_images

def verify_arguments(image):
    if image is None:
        st.error("Please choose an image above")
        st.stop()