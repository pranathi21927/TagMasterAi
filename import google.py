import google.generativeai as genai
import json
from PIL import Image
import io

API_KEY = "GEMINI_API_KEY"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)

def analyze_image(image_path):
    """Extracts metadata from an image using Google's Gemini Vision Pro."""
    
    # Load the image
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()

    # Convert image data into Gemini Vision format
    image = Image.open(io.BytesIO(img_data))
    
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

# Example Usage
image_path = "example.jpg"  # Change to your image file path
metadata = analyze_image(image_path)

# Output the JSON metadata
json_output = json.dumps(metadata, indent=4)
print(json_output)
