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