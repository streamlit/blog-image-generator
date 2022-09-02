import streamlit as st
from .lib.generate_images import generate_gradients, get_gradient_direction, generate_base64_image, resize_image

def render():
    images = []

    image1 = st.file_uploader("Choose the first image", help="Recommended size for the image: 1200x700 pixels")
    if image1 is not None:
        images.append(image1)

    image2 = st.file_uploader("Choose the second image", help="Recommended size for the image: 1200x700 pixels")
    if image2 is not None:
        images.append(image2)

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

    buffered_image1 = resize_image(images[0], 1200, 700)
    buffered_image2 = resize_image(images[1], 1200, 700)
    image1 = generate_base64_image(buffered_image1.getvalue())
    image2 = generate_base64_image(buffered_image2.getvalue())

    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):

        generated_images.append(f"""
            <svg width="1480" height="700" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g clip-path="url(#clip0_429_334)">

                    # Background
                    <rect width="1480" height="700" fill="url(#gradient)"/>

                    # 3 incomplete browser frames at the top
                    <g filter="url(#filter0_d_429_334)">
                        <g filter="url(#filter1_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M-434 -349C-440.627 -349 -446 -343.627 -446 -337V73C-446 79.6274 -440.627 85 -434 85H200C206.627 85 212 79.6274 212 73V-337C212 -343.627 206.627 -349 200 -349H-434ZM-415.765 -290.81C-419.078 -290.81 -421.765 -288.124 -421.765 -284.81V54.7542C-421.765 58.0679 -419.078 60.7542 -415.765 60.7542H181.764C185.078 60.7542 187.764 58.0679 187.764 54.7542V-284.81C187.764 -288.124 185.078 -290.81 181.764 -290.81H-415.765Z" fill="white"/>
                            <path d="M-434 -349.5C-440.904 -349.5 -446.5 -343.904 -446.5 -337V73C-446.5 79.9036 -440.904 85.5 -434 85.5H200C206.904 85.5 212.5 79.9036 212.5 73V-337C212.5 -343.904 206.904 -349.5 200 -349.5H-434ZM-421.265 -284.81C-421.265 -287.848 -418.802 -290.31 -415.765 -290.31H181.764C184.801 -290.31 187.264 -287.848 187.264 -284.81V54.7542C187.264 57.7917 184.801 60.2542 181.764 60.2542H-415.765C-418.802 60.2542 -421.265 57.7918 -421.265 54.7542V-284.81Z" stroke="#FAFAFA"/>
                        </g>
                    </g>

                    <g filter="url(#filter2_d_429_334)">
                        <g filter="url(#filter3_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M272 -349C265.373 -349 260 -343.627 260 -337V73C260 79.6274 265.373 85 272 85H906C912.627 85 918 79.6274 918 73V-337C918 -343.627 912.627 -349 906 -349H272ZM290.235 -290.81C286.922 -290.81 284.235 -288.124 284.235 -284.81V54.7542C284.235 58.0679 286.922 60.7542 290.235 60.7542H887.764C891.078 60.7542 893.764 58.0679 893.764 54.7542V-284.81C893.764 -288.124 891.078 -290.81 887.764 -290.81H290.235Z" fill="white"/>
                            <path d="M272 -349.5C265.096 -349.5 259.5 -343.904 259.5 -337V73C259.5 79.9036 265.096 85.5 272 85.5H906C912.904 85.5 918.5 79.9036 918.5 73V-337C918.5 -343.904 912.904 -349.5 906 -349.5H272ZM284.735 -284.81C284.735 -287.848 287.198 -290.31 290.235 -290.31H887.764C890.801 -290.31 893.264 -287.848 893.264 -284.81V54.7542C893.264 57.7917 890.801 60.2542 887.764 60.2542H290.235C287.198 60.2542 284.735 57.7918 284.735 54.7542V-284.81Z" stroke="#FAFAFA"/>
                        </g>
                    </g>

                    <g filter="url(#filter4_d_429_334)">
                        <g filter="url(#filter5_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M978 -349C971.373 -349 966 -343.627 966 -337V73C966 79.6274 971.373 85 978 85H1612C1618.63 85 1624 79.6274 1624 73V-337C1624 -343.627 1618.63 -349 1612 -349H978ZM996.235 -290.81C992.922 -290.81 990.235 -288.124 990.235 -284.81V54.7542C990.235 58.0679 992.922 60.7542 996.235 60.7542H1593.76C1597.08 60.7542 1599.76 58.0679 1599.76 54.7542V-284.81C1599.76 -288.124 1597.08 -290.81 1593.76 -290.81H996.235Z" fill="white"/>
                            <path d="M978 -349.5C971.096 -349.5 965.5 -343.904 965.5 -337V73C965.5 79.9036 971.096 85.5 978 85.5H1612C1618.9 85.5 1624.5 79.9036 1624.5 73V-337C1624.5 -343.904 1618.9 -349.5 1612 -349.5H978ZM990.735 -284.81C990.735 -287.848 993.198 -290.31 996.235 -290.31H1593.76C1596.8 -290.31 1599.26 -287.848 1599.26 -284.81V54.7542C1599.26 57.7917 1596.8 60.2542 1593.76 60.2542H996.235C993.198 60.2542 990.735 57.7918 990.735 54.7542V-284.81Z" stroke="#FAFAFA"/>
                        </g>
                    </g>

                    # 3 incomplete browser frames at the bottom
                    <g filter="url(#filter6_d_429_334)">
                        <g filter="url(#filter7_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M-354 615C-360.627 615 -366 620.373 -366 627V1037C-366 1043.63 -360.627 1049 -354 1049H280C286.627 1049 292 1043.63 292 1037V627C292 620.373 286.627 615 280 615H-354ZM-335.765 673.19C-339.078 673.19 -341.765 675.876 -341.765 679.19V1018.75C-341.765 1022.07 -339.078 1024.75 -335.765 1024.75H261.764C265.078 1024.75 267.764 1022.07 267.764 1018.75V679.19C267.764 675.876 265.078 673.19 261.764 673.19H-335.765Z" fill="white"/>
                            <path d="M-354 614.5C-360.904 614.5 -366.5 620.096 -366.5 627V1037C-366.5 1043.9 -360.904 1049.5 -354 1049.5H280C286.904 1049.5 292.5 1043.9 292.5 1037V627C292.5 620.096 286.904 614.5 280 614.5H-354ZM-341.265 679.19C-341.265 676.152 -338.802 673.69 -335.765 673.69H261.764C264.801 673.69 267.264 676.152 267.264 679.19V1018.75C267.264 1021.79 264.801 1024.25 261.764 1024.25H-335.765C-338.802 1024.25 -341.265 1021.79 -341.265 1018.75V679.19Z" stroke="#FAFAFA"/>
                        </g>
                    </g>

                    <g filter="url(#filter8_d_429_334)">
                        <g filter="url(#filter9_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M352 615C345.373 615 340 620.373 340 627V1037C340 1043.63 345.373 1049 352 1049H986C992.627 1049 998 1043.63 998 1037V627C998 620.373 992.627 615 986 615H352ZM370.235 673.19C366.922 673.19 364.235 675.876 364.235 679.19V1018.75C364.235 1022.07 366.922 1024.75 370.235 1024.75H967.764C971.078 1024.75 973.764 1022.07 973.764 1018.75V679.19C973.764 675.876 971.078 673.19 967.764 673.19H370.235Z" fill="white"/>
                            <path d="M352 614.5C345.096 614.5 339.5 620.096 339.5 627V1037C339.5 1043.9 345.096 1049.5 352 1049.5H986C992.904 1049.5 998.5 1043.9 998.5 1037V627C998.5 620.096 992.904 614.5 986 614.5H352ZM364.735 679.19C364.735 676.152 367.198 673.69 370.235 673.69H967.764C970.801 673.69 973.264 676.152 973.264 679.19V1018.75C973.264 1021.79 970.801 1024.25 967.764 1024.25H370.235C367.198 1024.25 364.735 1021.79 364.735 1018.75V679.19Z" stroke="#FAFAFA"/>
                        </g>
                        <ellipse cx="369.082" cy="644.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="390.895" cy="644.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="412.707" cy="644.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>

                    <g filter="url(#filter10_d_429_334)">
                        <g filter="url(#filter11_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M1058 615C1051.37 615 1046 620.373 1046 627V1037C1046 1043.63 1051.37 1049 1058 1049H1692C1698.63 1049 1704 1043.63 1704 1037V627C1704 620.373 1698.63 615 1692 615H1058ZM1076.24 673.19C1072.92 673.19 1070.24 675.876 1070.24 679.19V1018.75C1070.24 1022.07 1072.92 1024.75 1076.24 1024.75H1673.76C1677.08 1024.75 1679.76 1022.07 1679.76 1018.75V679.19C1679.76 675.876 1677.08 673.19 1673.76 673.19H1076.24Z" fill="white"/>
                            <path d="M1058 614.5C1051.1 614.5 1045.5 620.096 1045.5 627V1037C1045.5 1043.9 1051.1 1049.5 1058 1049.5H1692C1698.9 1049.5 1704.5 1043.9 1704.5 1037V627C1704.5 620.096 1698.9 614.5 1692 614.5H1058ZM1070.74 679.19C1070.74 676.152 1073.2 673.69 1076.24 673.69H1673.76C1676.8 673.69 1679.26 676.152 1679.26 679.19V1018.75C1679.26 1021.79 1676.8 1024.25 1673.76 1024.25H1076.24C1073.2 1024.25 1070.74 1021.79 1070.74 1018.75V679.19Z" stroke="#FAFAFA"/>
                        </g>
                        <ellipse cx="1075.08" cy="644.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="1096.9" cy="644.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="1118.71" cy="644.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>

                    # The two important ones at the center
                    <g filter="url(#filter12_d_429_334)">
                        <g filter="url(#filter13_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M70 133C63.3726 133 58 138.373 58 145V555C58 561.627 63.3726 567 70 567H704C710.627 567 716 561.627 716 555V145C716 138.373 710.627 133 704 133H70ZM88.2354 191.19C84.9216 191.19 82.2354 193.876 82.2354 197.19V536.754C82.2354 540.068 84.9216 542.754 88.2353 542.754H685.764C689.078 542.754 691.764 540.068 691.764 536.754V197.19C691.764 193.876 689.078 191.19 685.764 191.19H88.2354Z" fill="white"/>
                            
                            # Image
                            <rect x="82" y="189" width="610" height="355" rx="6" fill="url(#image-1)"/>

                            <path d="M70 132.5C63.0964 132.5 57.5 138.096 57.5 145V555C57.5 561.904 63.0964 567.5 70 567.5H704C710.904 567.5 716.5 561.904 716.5 555V145C716.5 138.096 710.904 132.5 704 132.5H70ZM82.7354 197.19C82.7354 194.152 85.1978 191.69 88.2354 191.69H685.764C688.801 191.69 691.264 194.152 691.264 197.19V536.754C691.264 539.792 688.801 542.254 685.764 542.254H88.2353C85.1978 542.254 82.7354 539.792 82.7354 536.754V197.19Z" stroke="#FAFAFA"/>
                        </g>
                        <ellipse cx="87.0825" cy="162.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="108.894" cy="162.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="130.708" cy="162.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                    
                    <g filter="url(#filter14_d_429_334)">
                        <g filter="url(#filter15_dd_429_334)">
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M776 133C769.373 133 764 138.373 764 145V555C764 561.627 769.373 567 776 567H1410C1416.63 567 1422 561.627 1422 555V145C1422 138.373 1416.63 133 1410 133H776ZM794.235 191.19C790.922 191.19 788.235 193.876 788.235 197.19V536.754C788.235 540.068 790.922 542.754 794.235 542.754H1391.76C1395.08 542.754 1397.76 540.068 1397.76 536.754V197.19C1397.76 193.876 1395.08 191.19 1391.76 191.19H794.235Z" fill="white"/>
                            
                            # Image
                            <rect x="789" y="189" width="610" height="355" rx="6" fill="url(#image-2)"/>

                            <path d="M776 132.5C769.096 132.5 763.5 138.096 763.5 145V555C763.5 561.904 769.096 567.5 776 567.5H1410C1416.9 567.5 1422.5 561.904 1422.5 555V145C1422.5 138.096 1416.9 132.5 1410 132.5H776ZM788.735 197.19C788.735 194.152 791.198 191.69 794.235 191.69H1391.76C1394.8 191.69 1397.26 194.152 1397.26 197.19V536.754C1397.26 539.792 1394.8 542.254 1391.76 542.254H794.235C791.198 542.254 788.735 539.792 788.735 536.754V197.19Z" stroke="#FAFAFA"/>
                        </g>
                        <ellipse cx="793.083" cy="162.095" rx="4.84715" ry="4.84916" fill="#FF6C6C"/>
                        <ellipse cx="814.894" cy="162.095" rx="4.84715" ry="4.84916" fill="#FFE312"/>
                        <ellipse cx="836.708" cy="162.095" rx="4.84715" ry="4.84916" fill="#3DD56D"/>
                    </g>
                </g>

                <defs>
                    # Filters and stuff
                    <filter id="filter0_d_429_334" x="-487" y="-386" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter1_dd_429_334" x="-487" y="-385" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter2_d_429_334" x="219" y="-386" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter3_dd_429_334" x="219" y="-385" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter4_d_429_334" x="925" y="-386" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter5_dd_429_334" x="925" y="-385" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter6_d_429_334" x="-407" y="578" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter7_dd_429_334" x="-407" y="579" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter8_d_429_334" x="299" y="578" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter9_dd_429_334" x="299" y="579" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter10_d_429_334" x="1005" y="578" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter11_dd_429_334" x="1005" y="579" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter12_d_429_334" x="17" y="96" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_334"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter13_dd_429_334" x="17" y="97" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="2"/>
                        <feGaussianBlur stdDeviation="6"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_334"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="5"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_429_334" result="effect2_dropShadow_429_334"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter14_d_429_334" x="723" y="96" width="724" height="500" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_334"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_334" result="shape"/>
                    </filter>
                    <filter id="filter15_dd_429_334" x="723" y="97" width="740" height="516" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="2"/>
                        <feGaussianBlur stdDeviation="6"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_334"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="5"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_429_334" result="effect2_dropShadow_429_334"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_334" result="shape"/>
                    </filter>
                    
                    <pattern id="image-1" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-1" x="0" y="0" width="610" height="360" xlink:href="data:image/jpeg;charset=utf-8;base64,{image1}" />
                    </pattern>
                    <pattern id="image-2" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-2" x="0" y="0" width="610" height="360" xlink:href="data:image/jpeg;charset=utf-8;base64,{image2}" />
                    </pattern>
                    
                    <clipPath id="clip0_429_334">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>

                    # Gradient
                    <linearGradient id="gradient" x1="{coordinates[0]}" y1="{coordinates[1]}" x2="{coordinates[2]}" y2="{coordinates[3]}">{gradients[i]}</linearGradient>
                    
                </defs>
            </svg>
        """.strip())

    return generated_images

def verify_arguments(images):
    MIN_IMAGES = 2

    if len(images) < MIN_IMAGES:
        st.error("Please choose at least two images")
        st.stop()
