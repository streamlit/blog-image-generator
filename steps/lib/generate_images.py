import streamlit as st
import base64
import random
from PIL import Image
import io

def generate_gradient():

  # Available gradients
  gradients = [
    ["#00C0F2", "#9BF8FE", "#C0FCD3"],
    ["#FFABAB", "#FFECB0", "#FFFFE1"],
    ["#FF6C6C", "#DBBBFF", "#C7EBFF"],
    ["#FFD16A", "#FFECB0", "#E6EAF1"],
    ["#FF8C8C", "#FFC7C7", "#C0FCD3"],
    ["#1C83E1", "#F5EBFF", "#F0F2F6"],
    ["#29B09D", "#DBBBFF", "#C0FCD3", "#DFFDE9"],
    ["#555867", "#FF6C6C", "#FFDEDE"],
    ["#A3A8B8", "#FFABAB", "#FFF0F0"],
    ["#B27EFF", "#DBBBFF", "#FFDEDE"],
    ["#20E7C5", "#F5EBFF", "#FFFFE1"],
    ["#FFE08E", "#DBBBFF", "#C7EBFF"],
    ["#60B4FF", "#FFC7C7", "#EBD6FF"],
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
    st.error(f'Image {image.name} is too small! Please add an image that is at least {container_width}px wide.')
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