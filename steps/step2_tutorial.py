import streamlit as st
from .lib.generate_images import generate_gradients, get_gradient_direction, generate_base64_image, resize_image

def render():
    images = []

    image1 = st.file_uploader("Choose front image", help="Recommended size: 1200x780 pixels", key="image2")
    if image1 != None:
        images.append(image1)

    image2 = st.file_uploader("Choose bottom image", help="Recommended size: 1200x780 pixels", key="image1")
    if image2 != None:
        images.append(image2)

    showCategory = st.checkbox('Show category text and icon')

    direction = st.selectbox(
        'Gradient direction',
        ['0 degrees (left-to-right)',
        '45 degrees (diagonal top-left-to-bottom-right)',
        '90 degrees (top-to-bottom)',
        '135 degrees (diagonal top-right-to-bottom-left)',
        '315 degrees (diagonal bottom-left-top-top-right)'
        ],
    )

    return [images, showCategory, direction]


def generate(images, category, gradient_direction):
    verify_arguments(images)

    buffered_image1 = resize_image(images[0], 1200, 780)
    buffered_image2 = resize_image(images[1], 1200, 780)
    bottom_image = generate_base64_image(buffered_image1.getvalue())
    front_image = generate_base64_image(buffered_image2.getvalue())

    generated_images = []
    gradients = generate_gradients()
    coordinates = get_gradient_direction(gradient_direction)

    for i in range(len(gradients) - 1):
        categoryContent = ''

        if category:
            categoryContent = f"""
                <path fill-rule="evenodd" clip-rule="evenodd" d="M1274 48C1250.8 48 1232 66.804 1232 90C1232 113.196 1250.8 132 1274 132H1390C1413.2 132 1432 113.196 1432 90C1432 66.804 1413.2 48 1390 48H1274ZM1273.5 60C1257.21 60 1244 73.2076 1244 89.5C1244 105.792 1257.21 119 1273.5 119H1274.5C1290.79 119 1304 105.792 1304 89.5C1304 73.2076 1290.79 60 1274.5 60H1273.5Z" fill="white"/>

                # Icon
                <path d="M1290.72 97.6472C1290.36 97.6472 1290.05 97.5303 1289.81 97.2966C1289.57 97.0628 1289.45 96.7672 1289.45 96.4097V86.0142L1274.49 93.8521C1274.29 93.9621 1274.09 94.0377 1273.89 94.0789C1273.7 94.1202 1273.48 94.1408 1273.26 94.1408C1273.03 94.1408 1272.82 94.1202 1272.64 94.0789C1272.46 94.0377 1272.26 93.9621 1272.07 93.8521L1256.64 85.643C1256.41 85.533 1256.25 85.3817 1256.15 85.1892C1256.05 84.9967 1256 84.7904 1256 84.5704C1256 84.3504 1256.05 84.1441 1256.15 83.9516C1256.25 83.7591 1256.41 83.6079 1256.64 83.4979L1272.02 75.33C1272.22 75.22 1272.42 75.1375 1272.62 75.0825C1272.82 75.0275 1273.03 75 1273.26 75C1273.48 75 1273.7 75.0275 1273.89 75.0825C1274.09 75.1375 1274.29 75.22 1274.49 75.33L1291.32 84.1991C1291.55 84.3367 1291.72 84.5017 1291.83 84.6942C1291.94 84.8867 1292 85.0929 1292 85.3129V96.4097C1292 96.7672 1291.88 97.0628 1291.64 97.2966C1291.4 97.5303 1291.09 97.6472 1290.72 97.6472V97.6472ZM1273.26 104C1273.03 104 1272.82 103.979 1272.62 103.938C1272.42 103.897 1272.22 103.821 1272.02 103.711L1262.25 98.5135C1261.85 98.2935 1261.53 97.991 1261.29 97.606C1261.05 97.221 1260.93 96.7947 1260.93 96.3272V89.1494L1271.51 94.7596L1272.36 95.1721C1272.65 95.3096 1272.94 95.3784 1273.26 95.3784C1273.57 95.3784 1273.87 95.3096 1274.17 95.1721C1274.47 95.0346 1274.76 94.8971 1275.04 94.7596L1285.58 89.1494V96.3272C1285.58 96.7947 1285.46 97.221 1285.22 97.606C1284.98 97.991 1284.66 98.2935 1284.26 98.5135L1274.49 103.711C1274.29 103.821 1274.09 103.897 1273.89 103.938C1273.7 103.979 1273.48 104 1273.26 104V104Z" fill="white"/>

                # Text
                <path d="M1316.96 83.696V81.0454H1330.88V83.696H1325.49V98.5H1322.35V83.696H1316.96Z" fill="#262730"/>
                <path d="M1340.23 92.9943V85.409H1343.32V98.5H1340.33V96.1733H1340.19C1339.89 96.9062 1339.41 97.5056 1338.73 97.9715C1338.06 98.4375 1337.23 98.6704 1336.25 98.6704C1335.39 98.6704 1334.64 98.4801 1333.98 98.0994C1333.32 97.713 1332.81 97.1534 1332.44 96.4204C1332.07 95.6818 1331.89 94.7897 1331.89 93.7443V85.409H1334.97V93.267C1334.97 94.0965 1335.2 94.7556 1335.66 95.2443C1336.11 95.7329 1336.71 95.9772 1337.45 95.9772C1337.9 95.9772 1338.34 95.8664 1338.77 95.6448C1339.19 95.4233 1339.54 95.0937 1339.81 94.6562C1340.09 94.213 1340.23 93.659 1340.23 92.9943Z" fill="#262730"/>
                <path d="M1353.27 85.409V87.7954H1345.74V85.409H1353.27ZM1347.6 82.2727H1350.68V94.5625C1350.68 94.9772 1350.75 95.2954 1350.87 95.517C1351 95.7329 1351.17 95.8806 1351.38 95.9602C1351.59 96.0397 1351.83 96.0795 1352.08 96.0795C1352.28 96.0795 1352.45 96.0653 1352.61 96.0369C1352.78 96.0085 1352.9 95.9829 1352.99 95.9602L1353.51 98.3721C1353.34 98.4289 1353.1 98.4914 1352.8 98.5596C1352.5 98.6278 1352.13 98.6676 1351.69 98.6789C1350.92 98.7017 1350.22 98.5852 1349.6 98.3295C1348.98 98.0681 1348.49 97.6647 1348.13 97.1193C1347.77 96.5738 1347.59 95.892 1347.6 95.0738V82.2727Z" fill="#262730"/>
                <path d="M1361.66 98.7556C1360.38 98.7556 1359.27 98.4744 1358.33 97.9119C1357.4 97.3494 1356.67 96.5625 1356.15 95.5511C1355.64 94.5397 1355.38 93.3579 1355.38 92.0056C1355.38 90.6534 1355.64 89.4687 1356.15 88.4517C1356.67 87.4346 1357.4 86.6448 1358.33 86.0823C1359.27 85.5198 1360.38 85.2386 1361.66 85.2386C1362.94 85.2386 1364.04 85.5198 1364.98 86.0823C1365.92 86.6448 1366.64 87.4346 1367.15 88.4517C1367.67 89.4687 1367.93 90.6534 1367.93 92.0056C1367.93 93.3579 1367.67 94.5397 1367.15 95.5511C1366.64 96.5625 1365.92 97.3494 1364.98 97.9119C1364.04 98.4744 1362.94 98.7556 1361.66 98.7556ZM1361.67 96.284C1362.37 96.284 1362.95 96.0937 1363.41 95.713C1363.88 95.3267 1364.22 94.8096 1364.45 94.1619C1364.69 93.5142 1364.8 92.7926 1364.8 91.9971C1364.8 91.196 1364.69 90.4715 1364.45 89.8238C1364.22 89.1704 1363.88 88.6505 1363.41 88.2642C1362.95 87.8778 1362.37 87.6846 1361.67 87.6846C1360.96 87.6846 1360.37 87.8778 1359.9 88.2642C1359.44 88.6505 1359.09 89.1704 1358.85 89.8238C1358.63 90.4715 1358.51 91.196 1358.51 91.9971C1358.51 92.7926 1358.63 93.5142 1358.85 94.1619C1359.09 94.8096 1359.44 95.3267 1359.9 95.713C1360.37 96.0937 1360.96 96.284 1361.67 96.284Z" fill="#262730"/>
                <path d="M1370.79 98.5V85.409H1373.78V87.5909H1373.92C1374.15 86.8352 1374.56 86.2528 1375.14 85.8437C1375.73 85.4289 1376.4 85.2215 1377.15 85.2215C1377.32 85.2215 1377.51 85.2301 1377.72 85.2471C1377.93 85.2585 1378.11 85.2784 1378.25 85.3068V88.1448C1378.12 88.0994 1377.92 88.0596 1377.63 88.0255C1377.35 87.9858 1377.08 87.9659 1376.82 87.9659C1376.26 87.9659 1375.75 88.088 1375.3 88.3323C1374.86 88.571 1374.51 88.9034 1374.26 89.3295C1374 89.7556 1373.87 90.2471 1373.87 90.8039V98.5H1370.79Z" fill="#262730"/>
                <path d="M1380.54 98.5V85.409H1383.63V98.5H1380.54ZM1382.09 83.5511C1381.61 83.5511 1381.19 83.3892 1380.83 83.0653C1380.48 82.7358 1380.3 82.3409 1380.3 81.8806C1380.3 81.4147 1380.48 81.0198 1380.83 80.696C1381.19 80.3664 1381.61 80.2017 1382.09 80.2017C1382.59 80.2017 1383.01 80.3664 1383.36 80.696C1383.71 81.0198 1383.88 81.4147 1383.88 81.8806C1383.88 82.3409 1383.71 82.7358 1383.36 83.0653C1383.01 83.3892 1382.59 83.5511 1382.09 83.5511Z" fill="#262730"/>
                <path d="M1390.81 98.7642C1389.98 98.7642 1389.23 98.6164 1388.57 98.321C1387.91 98.0198 1387.39 97.5767 1387 96.9914C1386.62 96.4062 1386.43 95.6846 1386.43 94.8267C1386.43 94.088 1386.56 93.4772 1386.84 92.9943C1387.11 92.5113 1387.48 92.125 1387.95 91.8352C1388.42 91.5454 1388.96 91.3267 1389.55 91.1789C1390.14 91.0255 1390.76 90.9147 1391.4 90.8465C1392.16 90.767 1392.79 90.696 1393.26 90.6335C1393.74 90.5653 1394.09 90.463 1394.3 90.3267C1394.52 90.1846 1394.64 89.9659 1394.64 89.6704V89.6193C1394.64 88.9772 1394.44 88.4801 1394.06 88.1278C1393.68 87.7755 1393.14 87.5994 1392.42 87.5994C1391.66 87.5994 1391.06 87.7642 1390.62 88.0937C1390.18 88.4233 1389.89 88.8125 1389.73 89.2613L1386.85 88.8522C1387.08 88.0568 1387.46 87.392 1387.98 86.8579C1388.5 86.3181 1389.14 85.9147 1389.9 85.6477C1390.65 85.375 1391.49 85.2386 1392.4 85.2386C1393.03 85.2386 1393.66 85.3125 1394.29 85.4602C1394.91 85.6079 1395.48 85.8522 1396 86.1931C1396.52 86.5284 1396.93 86.9858 1397.24 87.5653C1397.56 88.1448 1397.72 88.8693 1397.72 89.7386V98.5H1394.75V96.7017H1394.65C1394.46 97.0653 1394.2 97.4062 1393.86 97.7244C1393.52 98.0369 1393.1 98.2897 1392.59 98.4829C1392.08 98.6704 1391.49 98.7642 1390.81 98.7642ZM1391.61 96.4971C1392.23 96.4971 1392.77 96.375 1393.22 96.1306C1393.67 95.8806 1394.02 95.5511 1394.27 95.142C1394.52 94.7329 1394.64 94.2869 1394.64 93.8039V92.2613C1394.55 92.3409 1394.38 92.4147 1394.15 92.4829C1393.92 92.5511 1393.67 92.6108 1393.38 92.6619C1393.1 92.713 1392.82 92.7585 1392.54 92.7983C1392.26 92.838 1392.02 92.8721 1391.81 92.9005C1391.35 92.963 1390.94 93.0653 1390.58 93.2073C1390.21 93.3494 1389.93 93.5483 1389.72 93.8039C1389.51 94.0539 1389.4 94.3778 1389.4 94.7755C1389.4 95.3437 1389.61 95.7727 1390.02 96.0625C1390.44 96.3522 1390.97 96.4971 1391.61 96.4971Z" fill="#262730"/>
                <path d="M1404.15 81.0454V98.5H1401.06V81.0454H1404.15Z" fill="#262730"/>
            """

        generated_images.append(f"""
            <svg width="100%" height="100%" viewBox="0 0 1480 700" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g clip-path="url(#clip0_429_305)">

                    <rect width="1480" height="700" fill="url(#gradient)"/>

                    # Left browser
                    <g filter="url(#filter0_d_429_305)">
                        <g filter="url(#filter1_dd_429_305)">
                            <path d="M959 325C959 320.582 955.418 317 951 317H247V779H959V325Z" fill="url(#pattern1)"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M975 238C981.627 238 987 243.373 987 250V700H953C956.314 700 959 697.314 959 694V320C959 316.686 956.314 314 953 314H253C249.686 314 247 316.686 247 320V238H975ZM247 694C247 697.314 249.686 700 253 700H247V694Z" fill="white"/>
                            <path d="M987.5 700V700.5H987H953V700V699.5C956.038 699.5 958.5 697.038 958.5 694V320C958.5 316.962 956.038 314.5 953 314.5H253C249.962 314.5 247.5 316.962 247.5 320H247H246.5V238V237.5H247H975C981.904 237.5 987.5 243.096 987.5 250V700ZM247 700.5H246.5V700V694H247H247.5C247.5 697.038 249.962 699.5 253 699.5V700V700.5H247Z" stroke="#FAFAFA"/>
                        </g>
                        <circle r="6" transform="matrix(-1 0 0 1 953 276)" fill="#FF6C6C"/>
                        <circle r="6" transform="matrix(-1 0 0 1 925 276)" fill="#FFE312"/>
                        <circle r="6" transform="matrix(-1 0 0 1 897 276)" fill="#3DD56D"/>
                    </g>

                    # Right browser
                    <g filter="url(#filter2_d_429_305)">
                        <g filter="url(#filter3_dd_429_305)">
                            <path d="M712 246C712 241.582 708.418 238 704 238H0V700H712V246Z" fill="url(#pattern2)"/>
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M728 162C734.627 162 740 167.373 740 174V700H712V246C712 241.582 708.418 238 704 238H0V162H728Z" fill="white"/>
                            <path d="M740.5 700V700.5H740H712H711.5V700V246C711.5 241.858 708.142 238.5 704 238.5H0H-0.5V238V162V161.5H0H728C734.904 161.5 740.5 167.096 740.5 174V700Z" stroke="#FAFAFA"/>
                        </g>
                        <circle r="6" transform="matrix(-1 0 0 1 706 200)" fill="#FF6C6C"/>
                        <circle r="6" transform="matrix(-1 0 0 1 678 200)" fill="#FFE312"/>
                        <circle r="6" transform="matrix(-1 0 0 1 650 200)" fill="#3DD56D"/>
                    </g>

                    # Category text and icon
                    {categoryContent}
                </g>

                <defs>
                    # Filters and stuff
                    <filter id="filter0_d_429_305" x="206" y="201" width="806" height="528" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_305"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_305" result="shape"/>
                    </filter>
                    <filter id="filter1_dd_429_305" x="206" y="202" width="822" height="544" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="2"/>
                        <feGaussianBlur stdDeviation="6"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_305"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="5"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_429_305" result="effect2_dropShadow_429_305"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_305" result="shape"/>
                    </filter>
                    <filter id="filter2_d_429_305" x="-41" y="125" width="806" height="604" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dx="-8" dy="-4"/>
                        <feGaussianBlur stdDeviation="16"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0.960784 0 0 0 0 0.921569 0 0 0 0 1 0 0 0 0.16 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_305"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_429_305" result="shape"/>
                    </filter>
                    <filter id="filter3_dd_429_305" x="-41" y="126" width="822" height="620" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                        <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="2"/>
                        <feGaussianBlur stdDeviation="6"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.05 0"/>
                        <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_429_305"/>
                        <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
                        <feOffset dy="5"/>
                        <feGaussianBlur stdDeviation="20"/>
                        <feComposite in2="hardAlpha" operator="out"/>
                        <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0.258824 0 0 0 0 0.501961 0 0 0 0.25 0"/>
                        <feBlend mode="normal" in2="effect1_dropShadow_429_305" result="effect2_dropShadow_429_305"/>
                        <feBlend mode="normal" in="SourceGraphic" in2="effect2_dropShadow_429_305" result="shape"/>
                    </filter>

                    <pattern id="pattern1" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-1" x="480" y="0" width="1200" height="780" xlink:href="data:image/jpeg;charset=utf-8;base64,{front_image}" />
                    </pattern>
                    <pattern id="pattern2" patternContentUnits="userSpaceOnUse" width="100%" height="100%">
                        <image id="screenshot-2" x="0" y="0" width="1200" height="780" xlink:href="data:image/jpeg;charset=utf-8;base64,{bottom_image}" />
                    </pattern>

                    <clipPath id="clip0_429_305">
                        <rect width="1480" height="700" fill="white"/>
                    </clipPath>
                    
                    # Gradient
                    <linearGradient id="gradient" x1="0" y1="0" x2="1" y2="0" gradientTransform="rotate({coordinates[0]})">{gradients[i]}</linearGradient>
                </defs>
            </svg>
        """.strip())

    return generated_images

def verify_arguments(images):
    MIN_IMAGES = 2

    if len(images) < MIN_IMAGES:
        st.error("Please add at least two images")
        st.stop()
