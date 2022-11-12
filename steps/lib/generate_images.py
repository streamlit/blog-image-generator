# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import base64
from PIL import Image
import io
import re

def get_gradient_direction(direction):
    result = [int(d) for d in re.findall(r'-?\d+', direction)]
    return result

def generate_gradients():

  # Available HEX combinations
  gradients = [
    ["#00C0F2", "#9BF8FE", "#C0FCD3"],
    ["#FFABAB", "#FFECB0", "#FFFFE1"],
    ["#FF6C6C", "#DBBBFF", "#C7EBFF"],
    ["#FFD16A", "#FFECB0", "#E6EAF1"],
    ["#FF8C8C", "#FFC7C7", "#C0FCD3"],
    ["#1C83E1", "#A6DCFF", "#F5EBFF", "#F0F2F6"],
    ["#29B09D", "#DBBBFF", "#C0FCD3", "#DFFDE9"],
    ["#555867", "#FF8C8C", "#FFDEDE"],
    ["#A3A8B8", "#FFABAB", "#FFF0F0"],
    ["#B27EFF", "#DBBBFF", "#FFDEDE"],
    ["#93FFEE", "#F5EBFF", "#FFFFE1"],
    ["#FFE08E", "#DBBBFF", "#C7EBFF"],
    ["#60B4FF", "#EBD6FF", "#FFD9D9", "#FFC7C7"],
    ["#EBD6FF", "#D4B2FF", "#FFABAB"],
    ["#F0F2F6", "#FFFFC2", "#BAFFF7"],
    ["#FFFAE8", "#F0F2F6", "#C7EBFF", "#9AF8FF"],
    ["#E6EAF1", "#FFC7C7", "#FF2B2B"],
    ["#DFFDE9", "#93FFEE", "#9EF6BB"],
    ["#F5EBFF", "#BFC5D3"],
    ["#BAFFF7", "#7DEFA1"],
    ["#45F4D5", "#F0F2F6"],
    ["#C0FCD3", "#DCFFFB", "#FFF0F0"],
    ["#FF2B2B", "#FFABAB", "#FFFAE8"],
  ]

  out = []
  
  for i, gradient in enumerate(gradients):
    gradient = gradients[i]
    gradient_stops = []

    for index, color in enumerate(gradient):
      offset = round(index / len(gradient) * 100)
      gradient_stops.append(f'<stop stop-color="{color}" offset="{offset}%" />')

    outstr = ''.join(gradient_stops)
      
    out.append(outstr)

  return out

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