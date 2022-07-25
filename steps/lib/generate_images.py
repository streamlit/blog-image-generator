import streamlit as st
import base64
import random
from PIL import Image
import io

def generate_gradient():

  # Available gradients
  gradients = [
    ["#232526", "#414345"],
    ["#757F9A", "#D7DDE8"],
    ["#5C258D", "#4389A2"],
    ["#134E5E", "#71B280"],
    ["#2BC0E4", "#EAECC6"],
    ["#085078", "#85D8CE"],
    ["#4776E6", "#8E54E9"],
    ["#614385", "#516395"],
    ["#1F1C2C", "#928DAB"],
    ["#16222A", "#3A6073"],
    ["#FF8008", "#FFC837"],
    ["#1D976C", "#93F9B9"],
    ["#EB3349", "#F45C43"],
    ["#DD5E89", "#F7BB97"],
    ["#4CB8C4", "#3CD3AD"],
    ["#1FA2FF", "#12D8FA", "#A6FFCB"],
    ["#1D2B64", "#F8CDDA"],
    ["#FF512F", "#F09819"],
    ["#1A2980", "#26D0CE"],
    ["#AA076B", "#61045F"],
    ["#FF512F", "#DD2476"],
    ["#F09819", "#EDDE5D"],
    ["#403B4A", "#E7E9BB"],
    ["#E55D87", "#5FC3E4"],
    ["#003973", "#E5E5BE"],
    ["#CC95C0", "#DBD4B4", "#7AA1D2"],
    ["#3CA55C", "#B5AC49"],
    ["#348F50", "#56B4D3"],
    ["#DA22FF", "#9733EE"],
    ["#02AAB0", "#00CDAC"],
    ["#EDE574", "#E1F5C4"],
    ["#D31027", "#EA384D"],
    ["#16A085", "#F4D03F"],
    ["#603813", "#b29f94"],
    ["#e52d27", "#b31217"],
    ["#ff6e7f", "#bfe9ff"],
    ["#77A1D3", "#79CBCA", "#E684AE"],
    ["#314755", "#26a0da"],
    ["#2b5876", "#4e4376"],
    ["#e65c00", "#F9D423"],
    ["#2193b0", "#6dd5ed"],
    ["#cc2b5e", "#753a88"],
    ["#ec008c", "#fc6767"],
    ["#1488CC", "#2B32B2"],
    ["#00467F", "#A5CC82"],
    ["#076585", "#FFFFFF"],
    ["#BBD2C5", "#536976"],
    ["#9796f0", "#fbc7d4"],
    ["#B79891", "#94716B"],
    ["#BBD2C5", "#536976", "#292E49"],
    ["#536976", "#292E49"],
    ["#acb6e5", "#86fde8"],
    ["#FFE000", "#799F0C"],
    ["#00416A", "#E4E5E6"],
    ["#ffe259", "#ffa751"],
    ["#799F0C", "#ACBB78"],
    ["#5433FF", "#20BDFF", "#A5FECB"],
    ["#0052D4", "#4364F7", "#6fb1fc"],
    ["#334d50", "#cbcaa5"],
    ["#00416A", "#799F0C", "#FFE000"],
    ["#F7F8F8", "#ACBB78"],
    ["#FFE000", "#799F0C"],
    ["#00416A", "#E4E5E6"],
    ["#bdc3c7", "#2c3e50"],
    ["#ee9ca7", "#ffdde1"],
    ["#2193b0", "#6dd5ed"],
    ["#C6FFDD", "#FBD786", "#f7797d"],
    ["#0F2027", "#203A43", "#2c5364"],
    ["#12c2e9", "#c471ed", "#f64f59"],
    ["#b92b27", "#1565C0"],
    ["#373B44", "#4286f4"],
    ["#2980B9", "#6DD5FA", "#FFFFFF"],
    ["#FF0099", "#493240"],
    ["#aa4b6b", "#6b6b83", "#3b8d99"],
    ["#8E2DE2", "#4A00E0"],
    ["#1f4037", "#99f2c8"],
    ["#f953c6", "#b91d73"],
    ["#7F7FD5", "#86A8E7", "#91eae4"],
    ["#c31432", "#240b36"],
    ["#f12711", "#f5af19"],
    ["#659999", "#f4791f"],
    ["#dd3e54", "#6be585"],
    ["#8360c3", "#2ebf91"],
    ["#544a7d", "#ffd452"],
    ["#009FFF", "#ec2F4B"],
    ["#654ea3", "#eaafc8"],
    ["#FF416C", "#FF4B2B"],
    ["#8A2387", "#E94057", "#f27121"],
    ["#a8ff78", "#78ffd6"],
    ["#1E9600", "#FFF200", "#FF0000"],
    ["#ED213A", "#93291E"],
    ["#FDC830", "#F37335"],
    ["#00B4DB", "#0083B0"],
    ["#FFEFBA", "#FFFFFF"],
    ["#59C173", "#a17fe0", "#5d26c1"],
    ["#005AA7", "#FFFDE4"],
    ["#DA4453", "#89216B"],
    ["#636363", "#a2ab58"],
    ["#ad5389", "#3c1053"],
    ["#a8c0ff", "#3f2b96"],
    ["#333333", "#dd1818"],
    ["#4e54c8", "#8f94fb"],
    ["#355C7D", "#6C5B7B", "#C06C84"],
    ["#bc4e9c", "#f80759"],
    ["#40E0D0", "#FF8C00", "#FF0080"],
    ["#3E5151", "#DECBA4"],
    ["#11998e", "#38ef7d"],
    ["#108dc7", "#ef8e38"],
    ["#FC5C7D", "#6A82FB"],
    ["#FC466B", "#3F5EFB"],
    ["#c94b4b", "#4b134f"],
    ["#23074d", "#cc5333"],
    ["#fffbd5", "#b20a2c"],
    ["#0f0c29", "#302b63", "#24243e"],
    ["#00b09b", "#96c93d"],
    ["#D3CCE3", "#E9E4F0"],
    ["#3C3B3F", "#605C3C"],
    ["#CAC531", "#F3F9A7"],
    ["#800080", "#ffc0cb"],
    ["#00F260", "#0575E6"],
    ["#fc4a1a", "#f7b733"],
    ["#74ebd5", "#ACB6E5"],
    ["#6D6027", "#D3CBB8"],
    ["#03001e", "#7303c0", "#ec38bc", "#fdeff9"],
    ["#667db6", "#0082c8", "#ec38bc", "#667db6"],
    ["#ADA996", "#F2F2F2", "#dbdbdb", "#eaeaea"],
    ["#e1eec3", "#f05053"],
    ["#1a2a6c", "#b21f1f", "#fdbb2d"],
    ["#22c1c3", "#fdbb2d"],
    ["#ff9966", "#ff5e62"],
    ["#7F00FF", "#E100FF"],
    ["#C9D6FF", "#E2E2E2"],
    ["#396afc", "#2948ff"],
    ["#d9a7c7", "#fffcdc"],
    ["#0cebeb", "#20e3b2", "#29ffc6"],
    ["#06beb6", "#48b1bf"],
    ["#642B73", "#C6426E"],
    ["#1c92d2", "#f2fcfe"],
    ["#000000", "#0f9b0f"],
    ["#36D1DC", "#5B86E5"],
    ["#CB356B", "#BD3F32"],
    ["#3A1C71", "#D76D77", "#FFAF7B"],
    ["#283c86", "#45a247"],
    ["#EF3B36", "#ffffff"],
    ["#c0392b", "#8e44ad"],
    ["#159957", "#155799"],
    ["#000046", "#1CB5E0"],
    ["#007991", "#78ffd6"],
    ["#56CCF2", "#2F80ED"],
    ["#F2994A", "#F2C94C"],
    ["#EB5757", "#000000"],
    ["#E44D26", "#F16529"],
    ["#4AC29A", "#BDFFF3"],
    ["#B2FEFA", "#0ED2F7"],
    ["#30E8BF", "#FF8235"],
    ["#D66D75", "#E29587"],
    ["#20002c", "#cbb4d4"],
    ["#C33764", "#1D2671"],
    ["#F7971E", "#FFD200"],
    ["#34e89e", "#0f3443"],
    ["#6190E8", "#A7BFE8"],
    ["#44A08D", "#093637"],
    ["#200122", "#6f0000"],
    ["#0575E6", "#021B79"],
    ["#4568DC", "#B06AB3"],
    ["#43C6AC", "#191654"],
    ["#093028", "#237A57"],
    ["#43C6AC", "#F8FFAE"],
    ["#FFAFBD", "#ffc3a0"],
    ["#F0F2F0", "#000C40"],
    ["#E8CBC0", "#636FA4"],
    ["#DCE35B", "#45B649"],
    ["#c0c0aa", "#1cefff"],
    ["#9CECFB", "#65C7F7", "#0052D4"],
    ["#DBE6F6", "#C5796D"],
    ["#3494E6", "#EC6EAD"],
    ["#67B26F", "#4ca2cd"],
    ["#F3904F", "#3B4371"],
    ["#ee0979", "#ff6a00"],
    ["#A770EF", "#CF8BF3", "#FDB99B"],
    ["#41295a", "#2F0743"],
    ["#f4c4f3", "#fc67fa"],
    ["#00c3ff", "#ffff1c"],
    ["#ff7e5f", "#feb47b"],
    ["#fffc00", "#ffffff"],
    ["#ff00cc", "#333399"],
    ["#de6161", "#2657eb"],
    ["#ef32d9", "#89fffd"],
    ["#3a6186", "#89253e"],
    ["#4ECDC4", "#556270"],
    # Disco
  ]

  x = random.randint(0,len(gradients) - 1)
  gradient = gradients[x]
  out = []

  for i, color in enumerate(gradient):
    offset = round(i / len(gradient) * 100)
    out.append(f'<stop stop-color="{color}" offset="{offset}%" />')

  outstr = ''.join(out)

  return outstr

def resize_image(image, container_width, container_height):
  # Image conversion stuff
  img_data = image.read()
  im = Image.open(io.BytesIO(img_data))
  if im.mode in ("RGBA", "P"):
    im = im.convert("RGB")
  
  # Calculations to ensure object-fit: cover; works as expected
  width  = im.size[0]
  height = im.size[1]
  aspect = width / float(height)
  ideal_aspect = container_width / float(container_height)

  # Throw an error if image is too small
  if(width < container_width):
    st.error(f'Image is too small! Please add an image that is at least {container_width}px wide.')
    st.stop()

  # Conditions to check the aspect ratios...
  if aspect > ideal_aspect:
      # And crop the left and right edges:
      new_width = int(ideal_aspect * height)
      offset = (width - new_width) / 2
      resize = (offset, 0, width - offset, height)
  else:
      # Or crop the top and bottom:
      new_height = int(width / ideal_aspect)
      offset = (height - new_height) / 2
      resize = (0, offset, width, height - offset)

  # Do the actual cropping/resizing
  thumb = im.crop(resize).resize((container_width, container_height), Image.ANTIALIAS)
  
  # And finally store the new image as a JPG
  buffered = io.BytesIO()
  thumb.save(buffered, 'jpeg', quality=80)
  return buffered

def generate_base64_image(image):
  image_string = base64.standard_b64encode(image)
  decoded = image_string.decode('utf-8')
  
  return decoded