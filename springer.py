import requests
import os
from PIL import Image

# Set your Springer API key
api_key = "YOUR_API_KEY"

# Set the DOI of the article you want to retrieve images from
doi = "10.1007/springer_crossmark_policy"

# Set the base URL for the Springer API
base_url = "http://api.springer.com/openaccess"

# Construct the URL for the article metadata
metadata_url = f"{base_url}/metadata/json?api_key={api_key}&doi={doi}"

# Make a GET request to the metadata URL and retrieve the JSON data
metadata_response = requests.get(metadata_url)
metadata_json = metadata_response.json()

# Find the image URLs in the metadata JSON
image_urls = []
for item in metadata_json["records"][0]["images"]:
    image_urls.append(item["url"])

# Create a directory to save the images
os.makedirs("article_images", exist_ok=True)

# Download and save each image
for i, url in enumerate(image_urls):
    image_response = requests.get(url)
    image_path = f"article_images/image_{i}.jpg"
    with open(image_path, "wb") as f:
        f.write(image_response.content)

# Open and display the first image
image = Image.open("article_images/image_0.jpg")
image.show()
