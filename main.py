import streamlit as st
import requests

# Prepare API key and API url
api = "4YJ4MvcwjnUqCf2FYqooYDXYTFh2oxwxwFcY7Zom"
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

# Get request data as a dictionary
response = requests.get(url)
data = response.json()

# Extract the image url, title, and description from the dictionary
title = data["title"]
image = data["url"]
description = data["explanation"]

# Alternative code to download the image
# image_url = requests.get(image)
# with open("image.jpg", "wb") as file:
#      file.write(image_url.content)



st.header(title)
st.image(image)
# st.image("image.jpg")
st.write(description)



