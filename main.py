import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY")

url = "https://api.nasa.gov/planetary/apod?" \
    f"api_key={API_KEY}"

response = requests.get(url)
data = response.json()

title = "NASA APOD"
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "image.png"
response_img = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response_img.content)

st.title(title)
st.image(image_filepath, caption=explanation)