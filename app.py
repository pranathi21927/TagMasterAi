import google.generativeai as genai
import json
import streamlit as st
from PIL import Image
import io

# Set up Google Gemini API
API_KEY = "AIzaSyA-IyzLZUu9tKqSkt7xyi6vwEwAFrO4g0Q"
genai.configure(api_key=API_KEY)

def analyze_image(image_data):
    """Extracts metadata from an image using Google's Gemini Vision Pro."""
    # Convert image data into Gemini Vision format
    image = Image.open(io.BytesIO(image_data))

    # Call Gemini Vision API
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([image], stream=False)

    # Parse API Response
    if response.text:
        metadata = {
            "tags": response.text.split(", "),  # Simple parsing (improve as needed)
            "full_description": response.text
        }
    else:
        metadata = {"error": "No response from Gemini Vision"}

    return metadata

# Streamlit UI
st.title("Image Metadata Analysis using Gemini Vision Pro")
st.write("Upload an image and receive metadata extracted from Google's Gemini Vision Pro.")

# Image upload functionality
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    image_data = uploaded_file.read()

    # Display the image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Call the analyze_image function
    metadata = analyze_image(image_data)

    # Display metadata
    st.subheader("Metadata:")
    st.json(metadata)  # Display the result as JSON

