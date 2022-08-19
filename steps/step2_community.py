import streamlit as st
from .lib.generate_images import generate_gradient, generate_base64_image, resize_image

def render():
    images = []

    image1 = st.file_uploader("Choose the first image", help="Recommended size for the image: 610x350 pixels")
    if image1 is not None:
        images.append(image1)

    image2 = st.file_uploader("Choose the second image", help="Recommended size for the image: 610x350 pixels")
    if image2 is not None:
        images.append(image2)

    return [images]


def generate(images):
    verify_arguments(images)

    buffered_image1 = resize_image(images[0], 610, 350)
    buffered_image2 = resize_image(images[1], 610, 350)
    image1 = generate_base64_image(buffered_image1.getvalue())
    image2 = generate_base64_image(buffered_image2.getvalue())
    
    generated_images = []
    for i in range(4):
        gradient = generate_gradient()

        generated_images.append(f"""
            <svg width="100%" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g clip-path="url(#clip0_305_225)">
                    <rect width="1480" height="700" fill="url(#gradient)"/>
                    <g filter="url(#filter0_d_305_225)">
                        <path d="M-446 -337C-446 -343.627 -440.627 -349 -434 -349H200C206.627 -349 212 -343.627 212 -337V73C212 79.6274 206.627 85 200 85H-434C-440.627 85 -446 79.6274 -446 73V-337Z" fill="white"/>
                        <rect x="-421.265" y="-290.31" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                    </g>
                    <g filter="url(#filter1_d_305_225)">
                        <path d="M260 -337C260 -343.627 265.373 -349 272 -349H906C912.627 -349 918 -343.627 918 -337V73C918 79.6274 912.627 85 906 85H272C265.373 85 260 79.6274 260 73V-337Z" fill="white"/>
                        <rect x="284.735" y="-290.31" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                    </g>
                    <g filter="url(#filter2_d_305_225)">
                        <path d="M966 -337C966 -343.627 971.373 -349 978 -349H1612C1618.63 -349 1624 -343.627 1624 -337V73C1624 79.6274 1618.63 85 1612 85H978C971.373 85 966 79.6274 966 73V-337Z" fill="white"/>
                        <rect x="990.735" y="-290.31" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                    </g>
                    <g filter="url(#filter3_d_305_225)">
                        <path d="M-366 627C-366 620.373 -360.627 615 -354 615H280C286.627 615 292 620.373 292 627V1037C292 1043.63 286.627 1049 280 1049H-354C-360.627 1049 -366 1043.63 -366 1037V627Z" fill="white"/>
                        <rect x="-341.265" y="673.69" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                    </g>
                    <g filter="url(#filter4_d_305_225)">
                        <path d="M58 145C58 138.373 63.3726 133 70 133H704C710.627 133 716 138.373 716 145V555C716 561.627 710.627 567 704 567H70C63.3726 567 58 561.627 58 555V145Z" fill="white"/>
                        <rect x="82.7354" y="191.69" width="608.529" height="350.564" rx="5.5" fill="url(#pattern1)" stroke="#F0F2F6"/>
                        <ellipse cx="87.0825" cy="162.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="108.895" cy="162.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="130.708" cy="162.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                    <g filter="url(#filter5_d_305_225)">
                        <path d="M340 627C340 620.373 345.373 615 352 615H986C992.627 615 998 620.373 998 627V1037C998 1043.63 992.627 1049 986 1049H352C345.373 1049 340 1043.63 340 1037V627Z" fill="white"/>
                        <rect x="364.735" y="673.69" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                        <ellipse cx="369.082" cy="644.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="390.895" cy="644.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="412.707" cy="644.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                    <g filter="url(#filter6_d_305_225)">
                        <path d="M764 145C764 138.373 769.373 133 776 133H1410C1416.63 133 1422 138.373 1422 145V555C1422 561.627 1416.63 567 1410 567H776C769.373 567 764 561.627 764 555V145Z" fill="white"/>
                        <rect x="788.735" y="191.69" width="608.529" height="350.564" rx="5.5" fill="url(#pattern2)" stroke="#F0F2F6"/>
                        <ellipse cx="793.083" cy="162.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="814.895" cy="162.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="836.707" cy="162.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                    <g filter="url(#filter7_d_305_225)">
                        <path d="M1046 627C1046 620.373 1051.37 615 1058 615H1692C1698.63 615 1704 620.373 1704 627V1037C1704 1043.63 1698.63 1049 1692 1049H1058C1051.37 1049 1046 1043.63 1046 1037V627Z" fill="white"/>
                        <rect x="1070.74" y="673.69" width="608.529" height="350.564" rx="5.5" fill="#FAFAFA" stroke="#F0F2F6"/>
                        <ellipse cx="1075.08" cy="644.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="1096.9" cy="644.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="1118.71" cy="644.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                </g>

                <defs>
                    <filter id="filter0_d_305_225" x="-486" y="-385" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <filter id="filter1_d_305_225" x="220" y="-385" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <filter id="filter2_d_305_225" x="926" y="-385" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <filter id="filter3_d_305_225" x="-406" y="579" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <filter id="filter4_d_305_225" x="18" y="97" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <pattern id="pattern1" patternContentUnits="objectBoundingBox" width="1" height="1">
                        <use xlink:href="#screenshot-1" transform="translate(-0.01) scale(0.000590125 0.000948461)"/>
                    </pattern>
                    <filter id="filter5_d_305_225" x="300" y="579" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <filter id="filter6_d_305_225" x="724" y="97" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <pattern id="pattern2" patternContentUnits="objectBoundingBox" width="1" height="1">
                        <use xlink:href="#screenshot-2" transform="translate(-0.01) scale(0.00059 0.000925712)"/>
                    </pattern>
                    <filter id="filter7_d_305_225" x="1006" y="579" width="722" height="498" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_305_225"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_305_225" result="shape"/>
                    </filter>
                    <clipPath id="clip0_305_225">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>
                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0" gradientTransform="rotate(-45)">{gradient}</linearGradient>
                    # Screenshot
                    <image id="screenshot-1" width="1728" height="1078" xlink:href="data:image/jpeg;charset=utf-8;base64,{image1}" />
                    <image id="screenshot-2" width="1728" height="1078" xlink:href="data:image/jpeg;charset=utf-8;base64,{image2}" />
                </defs>
            </svg>
        """.strip())
    
    return generated_images

def verify_arguments(images):
    MIN_IMAGES = 2

    if len(images) < MIN_IMAGES:
        st.error("Please choose at least two images")
        st.stop()