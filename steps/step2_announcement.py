import streamlit as st
from .lib.generate_images import generate_gradient, generate_base64_image, resize_image
from PIL import Image
import io

def render():
    image = st.file_uploader("Choose an image", help="Recommended size: 1300x825 pixels")
    return [image]


def generate(image):
    verify_arguments(image)

    # Generate gradient
    gradient = generate_gradient()

    # Get image byte data, resize and generate the base64 encoded version
    buffered = resize_image(image, 1300, 825)
    image = generate_base64_image(buffered.getvalue())

    return f"""
        <svg width="100%" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <g clip-path="url(#clip0_173_52)">
                <rect width="1480" height="700" fill="url(#gradient)"/>
                <g filter="url(#filter0_d_173_52)">
                    <g opacity="0.98" filter="url(#filter1_d_173_52)" transform="translate(0, 24)">
                        <path d="M64 76C64 69.3726 69.3726 64 76 64H1404C1410.63 64 1416 69.3726 1416 76V700H64V76Z" fill="white"/>
                    </g>
                    <path d="M96 188C96 183.582 99.5817 180 104 180H1376C1380.42 180 1384 183.582 1384 188V700H96V188Z" fill="url(#pattern1)"/>
                    # Browser circles
                    <g transform="translate(0, -32)">
                        <circle cx="106" cy="170" r="10" fill="#FF6C6C"/>
                        <circle cx="146.8" cy="170" r="10" fill="#FFE312"/>
                        <circle cx="187.6" cy="170" r="10" fill="#3DD56D"/>
                    </g>
                </g>
            </g>
            
            <defs>
                # Opacity and drop shadow filters for browser window
                <filter id="filter0_d_173_52" x="8" y="6" width="1460" height="744" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                    <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                    <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                    <feOffset dx="-2" dy="-4"/>
                    <feGaussianBlur stdDeviation="27"/>
                    <feComposite in2="hardAlpha" operator="out"/>
                    <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                    <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_173_52"/>
                    <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_173_52" result="shape"/>
                </filter>
                <filter id="filter1_d_173_52" x="32" y="36" width="1416" height="700" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                    <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                    <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                    <feOffset dy="4"/>
                    <feGaussianBlur stdDeviation="16"/>
                    <feComposite in2="hardAlpha" operator="out"/>
                    <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.12 0"/>
                    <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_173_52"/>
                    <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_173_52" result="shape"/>
                </filter>
                <pattern id="pattern1" patternContentUnits="objectBoundingBox" width="1" height="1">
                    <use xlink:href="#screenshot" transform="translate(0 0) scale(0.000578704 0.0014334)"/>
                </pattern>
                <clipPath id="clip0_173_52">
                    <rect width="1480" height="700" fill="white"/>
                </clipPath>
                # Gradient
                <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0">{gradient}</linearGradient>
                # Screenshot
                <image id="screenshot" width="1728" height="1078" xlink:href="data:image/jpeg;charset=utf-8;base64,{image}" />
            </defs>
        </svg>
    """.strip()

def verify_arguments(image):
    if image is None:
        st.error("Please choose an image above")
        st.stop()