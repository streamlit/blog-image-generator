import streamlit as st
from .lib.generate_images import generate_gradients, get_gradient_direction, generate_base64_image, resize_image
from PIL import Image
import io

def render():
    image = st.file_uploader("Choose an image", help="Recommended size: 1300x540 pixels")

    direction = st.selectbox(
        'Gradient direction',
        ['0 degrees (left-to-right)',
        '45 degrees (diagonal top-left-to-bottom-right)',
        '90 degrees (top-to-bottom)',
        '135 degrees (diagonal top-right-to-bottom-left)',
        '315 degrees (diagonal bottom-left-top-top-right)'
        ],
    )

    return [image, direction]


def generate(image, gradient_direction):
    verify_arguments(image)

    # Get image byte data, resize and generate the base64 encoded version
    buffered = resize_image(image, 1290, 540)
    image = generate_base64_image(buffered.getvalue())

    # Generate all images
    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):

        generated_images.append(f"""
            <svg width="1480" height="700" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

                # Group
                <g clip-path="url(#clip0_416_265)">

                    # White background
                    <rect width="1480" height="700" fill="white"/>

                    # Gradient
                    <rect width="1480" height="700" fill="url(#gradient)"/>

                    # Browser styles
                    <g filter="url(#filter0_dd_416_265)">
                        # Path to image
                        <image id="screenshot" x="95" y="160" width="1290" height="540" xlink:href="data:image/jpeg;charset=utf-8;base64,{image}" />

                        # Background
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M76 64C69.3726 64 64 69.3726 64 76V701H1416V76C1416 69.3726 1410.63 64 1404 64H76ZM104 162C99.5817 162 96 165.582 96 170V701H1384V170C1384 165.582 1380.42 162 1376 162H104Z" fill="white"/>

                        # Stroke
                        <path d="M63.5 701V701.5H64H95.5H96H1384H1384.5H1416H1416.5V701V76C1416.5 69.0964 1410.9 63.5 1404 63.5H76C69.0964 63.5 63.5 69.0964 63.5 76V701ZM1383.5 700.5H96.5V170C96.5 165.858 99.8579 162.5 104 162.5H1376C1380.14 162.5 1383.5 165.858 1383.5 170V700.5Z" stroke="#FAFAFA"/>
                    </g>

                    # Circles
                    <circle cx="106" cy="122" r="10" fill="#FF6C6C"/>
                    <circle cx="147" cy="122" r="10" fill="#FFE312"/>
                    <circle cx="188" cy="122" r="10" fill="#3DD56D"/>
                </g>

                # Definitions
                <defs>

                    # Filters
                    <filter id="filter0_dd_416_265" x="24" y="29" width="1432" height="716" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="2"/>
                        <feGaussianBlur stdDeviation="6"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_416_265"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="5"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_416_265" result="effect2_dropShadow_416_265"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_416_265" result="shape"/>
                    </filter>

                    # Image
                    <pattern id="pattern0" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot" x="0" y="0" width="1290" height="520" xlink:href="data:image/jpeg;charset=utf-8;base64,{image}" />
                    </pattern>

                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0" gradientTransform="rotate({coordinates[0]})">{gradients[i]}</linearGradient>

                    # Browser clip path
                    <clipPath id="clip0_416_265">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>
                </defs>
            </svg>
        """.strip())

    return generated_images

def verify_arguments(image):
    if image is None:
        st.error("Please choose an image above")
        st.stop()
