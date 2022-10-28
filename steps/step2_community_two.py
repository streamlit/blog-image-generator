import streamlit as st
from .lib.generate_images import generate_gradients, get_gradient_direction, generate_base64_image, resize_image

def render():
    images = []

    image1 = st.file_uploader("Choose the left image", help="Recommended size for the image: 1400x1000 pixels", key="image1")
    if image1 is not None:
        images.append(image1)

    image2 = st.file_uploader("Choose the top-right image", help="Recommended size for the image: 1200x700 pixels", key="image2")
    if image2 is not None:
        images.append(image2)
    
    image3 = st.file_uploader("Choose the bottom-right image", help="Recommended size for the image: 1200x440 pixels", key="image3")
    if image3 is not None:
        images.append(image3)

    direction = st.selectbox(
        'Gradient direction',
        ['0 degrees',
        '45 degrees',
        '90 degrees',
        '135 degrees',
        '180 degrees',
        '225 degrees',
        '270 degrees',
        '315 degrees'
        ],
    )

    return [images, direction]


def generate(images, gradient_direction):
    verify_arguments(images)

    buffered_image1 = resize_image(images[0], 1400, 1000)
    buffered_image2 = resize_image(images[1], 1200, 700)
    buffered_image3 = resize_image(images[2], 1200, 440)
    image1 = generate_base64_image(buffered_image1.getvalue())
    image2 = generate_base64_image(buffered_image2.getvalue())
    image3 = generate_base64_image(buffered_image3.getvalue())

    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):

        generated_images.append(f"""
            <svg width="1480" height="700" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g clip-path="url(#clip0_438_607)">

                    # Background
                    <rect width="1480" height="700" fill="url(#gradient)"/>

                    # Left browser
                    <g filter="url(#filter0_d_438_607)">
                        <g filter="url(#filter1_dd_438_607)">
                            <rect x="0" y="123" width="700" height="500" rx="6" fill="url(#image-1)"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M714 48C720.627 48 726 53.3726 726 60V640C726 646.627 720.627 652 714 652H-2V48H714ZM7 124C2.58173 124 -1 127.582 -1 132V616C-1 620.418 2.58173 624 7 624H691C695.418 624 699 620.418 699 616V132C699 127.582 695.418 124 691 124H7Z" fill="white"/>
                            <path d="M-2.5 652V652.5H-2H714C720.904 652.5 726.5 646.904 726.5 640V60C726.5 53.0964 720.904 47.5 714 47.5H-2H-2.5V48V652ZM-0.5 132C-0.5 127.858 2.85787 124.5 7 124.5H691C695.142 124.5 698.5 127.858 698.5 132V616C698.5 620.142 695.142 623.5 691 623.5H7C2.85787 623.5 -0.5 620.142 -0.5 616V132Z" stroke="#FAFAFA"/>
                        </g>
                        <circle r="6" transform="matrix(-1 0 0 1 692 86)" fill="#FF6C6C"/>
                        <circle r="6" transform="matrix(-1 0 0 1 664 86)" fill="#FFE312"/>
                        <circle r="6" transform="matrix(-1 0 0 1 636 86)" fill="#3DD56D"/>
                    </g>

                    # Top-right browser
                    <g filter="url(#filter2_d_438_607)">
                        <g filter="url(#filter3_dd_438_607)">
                            <rect x="799" y="-2" width="610" height="355" rx="6" fill="url(#image-2)"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M786 -59C779.373 -59 774 -53.6274 774 -47V363C774 369.627 779.373 375 786 375H1420C1426.63 375 1432 369.627 1432 363V-47C1432 -53.6274 1426.63 -59 1420 -59H786ZM804.235 -0.810059C800.922 -0.810059 798.235 1.87624 798.235 5.18995V344.754C798.235 348.068 800.922 350.754 804.235 350.754H1401.76C1405.08 350.754 1407.76 348.068 1407.76 344.754V5.18994C1407.76 1.87623 1405.08 -0.810059 1401.76 -0.810059H804.235Z" fill="white"/>
                            <path d="M786 -59.5C779.096 -59.5 773.5 -53.9036 773.5 -47V363C773.5 369.904 779.096 375.5 786 375.5H1420C1426.9 375.5 1432.5 369.904 1432.5 363V-47C1432.5 -53.9036 1426.9 -59.5 1420 -59.5H786ZM798.735 5.18995C798.735 2.15238 801.198 -0.310059 804.235 -0.310059H1401.76C1404.8 -0.310059 1407.26 2.15237 1407.26 5.18994V344.754C1407.26 347.792 1404.8 350.254 1401.76 350.254H804.235C801.198 350.254 798.735 347.792 798.735 344.754V5.18995Z" stroke="#FAFAFA"/>
                        </g>
                    </g>

                    # Bottom-right browser
                    <g filter="url(#filter4_d_438_607)">
                        <g filter="url(#filter5_dd_438_607)">
                            <rect x="799" y="475" width="610" height="230" rx="6" fill="url(#image-3)"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M786 423C779.373 423 774 428.373 774 435V845C774 851.627 779.373 857 786 857H1420C1426.63 857 1432 851.627 1432 845V435C1432 428.373 1426.63 423 1420 423H786ZM804.235 481.19C800.922 481.19 798.235 483.876 798.235 487.19V826.754C798.235 830.068 800.922 832.754 804.235 832.754H1401.76C1405.08 832.754 1407.76 830.068 1407.76 826.754V487.19C1407.76 483.876 1405.08 481.19 1401.76 481.19H804.235Z" fill="white"/>
                            <path d="M786 422.5C779.096 422.5 773.5 428.096 773.5 435V845C773.5 851.904 779.096 857.5 786 857.5H1420C1426.9 857.5 1432.5 851.904 1432.5 845V435C1432.5 428.096 1426.9 422.5 1420 422.5H786ZM798.735 487.19C798.735 484.152 801.198 481.69 804.235 481.69H1401.76C1404.8 481.69 1407.26 484.152 1407.26 487.19V826.754C1407.26 829.792 1404.8 832.254 1401.76 832.254H804.235C801.198 832.254 798.735 829.792 798.735 826.754V487.19Z" stroke="#FAFAFA"/>
                        </g>
                        <path d="M807.43 452.095C807.43 454.497 805.483 456.444 803.082 456.444C800.682 456.444 798.735 454.497 798.735 452.095C798.735 449.693 800.682 447.746 803.082 447.746C805.483 447.746 807.43 449.693 807.43 452.095Z" fill="#FF6C6C" stroke="#FAFAFA"/>
                        <path d="M829.241 452.095C829.241 454.497 827.295 456.444 824.894 456.444C822.493 456.444 820.547 454.497 820.547 452.095C820.547 449.693 822.493 447.746 824.894 447.746C827.295 447.746 829.241 449.693 829.241 452.095Z" fill="#FFE312" stroke="#FAFAFA"/>
                        <path d="M851.055 452.095C851.055 454.497 849.108 456.444 846.707 456.444C844.307 456.444 842.36 454.497 842.36 452.095C842.36 449.693 844.307 447.746 846.707 447.746C849.108 447.746 851.055 449.693 851.055 452.095Z" fill="#3DD56D" stroke="#FAFAFA"/>
                    </g>
                </g>

                <defs>
                    # Filters and stuff
                    <filter id="filter0_d_438_607" x="-43" y="11" width="794" height="670" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_438_607" result="shape"/>
                    </filter>
                    <filter xmlns="http://www.w3.org/2000/svg" id="filter1_dd_438_607" x="-43" y="12" width="810" height="686" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_438_607" result="effect2_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_438_607" result="shape"/>
                    </filter>
                    <filter id="filter2_d_438_607" x="733" y="-96" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_438_607" result="shape"/>
                    </filter>
                    <filter xmlns="http://www.w3.org/2000/svg" id="filter3_dd_438_607" x="733" y="-95" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_438_607" result="effect2_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_438_607" result="shape"/>
                    </filter>
                    <filter id="filter4_d_438_607" x="733" y="386" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_438_607" result="shape"/>
                    </filter>
                    <filter xmlns="http://www.w3.org/2000/svg" id="filter5_dd_438_607" x="733" y="387" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_438_607"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_438_607" result="effect2_dropShadow_438_607"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_438_607" result="shape"/>
                    </filter>

                    # Image definitions
                    <pattern id="image-1" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-1" x="0" y="0" width="700" height="500" xlink:href="data:image/jpeg;charset=utf-8;base64,{image1}" />
                    </pattern>
                    <pattern id="image-2" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-2" x="0" y="0" width="610" height="360" xlink:href="data:image/jpeg;charset=utf-8;base64,{image2}" />
                    </pattern>
                    <pattern id="image-3" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-3" x="0" y="0" width="610" height="230" xlink:href="data:image/jpeg;charset=utf-8;base64,{image3}" />
                    </pattern>
                    
                    <clipPath id="clip0_438_607">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>

                    # Gradient
                    <linearGradient id="gradient" x1="{coordinates[0]}" y1="{coordinates[1]}" x2="{coordinates[2]}" y2="{coordinates[3]}">{gradients[i]}</linearGradient>
                    
                </defs>
            </svg>
        """.strip())

    return generated_images

def verify_arguments(images):
    MIN_IMAGES = 3

    if len(images) < MIN_IMAGES:
        st.error("Please choose at least three images")
        st.stop()
