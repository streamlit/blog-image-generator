import streamlit as st
import base64
import random

def generate_gradient():
  # Get a random number for the gradient
  x = random.randint(0,335)

  with open(f'img/gradients/{x}.jpg', "rb") as img_file:
    image_string = base64.standard_b64encode(img_file.read())
    decoded = image_string.decode('utf-8')

    return decoded

def generate_image(image):
  image_string = base64.standard_b64encode(image.read())
  decoded = image_string.decode('utf-8')
  
  return decoded