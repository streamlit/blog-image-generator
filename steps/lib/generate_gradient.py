import streamlit as st
import base64
import random

def get_encoded_gradient():
  # Get a random number for the gradient
  x = random.randint(0,335)

  # Base64 encoding for gradient
  with open(f'img/gradients/{x}.jpg', "rb") as img_file:
    image_string = base64.standard_b64encode(img_file.read())
    decoded = image_string.decode('utf-8')

    return decoded