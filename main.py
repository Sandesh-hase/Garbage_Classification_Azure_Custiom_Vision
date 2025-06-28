from msrest.authentication import ApiKeyCredentials
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from PIL import Image, ImageDraw, ImageFont
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure config
PREDICTION_KEY = os.getenv("PREDICTION_KEY")
ENDPOINT = os.getenv("ENDPOINT")
PROJECT_ID = os.getenv("PROJECT_ID")
PUBLISHED_NAME = os.getenv("PUBLISHED_NAME")
IMAGE_PATH = "data/test/paper98.jpg"

# Authenticate prediction client
credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
prediction_client = CustomVisionPredictionClient(endpoint=ENDPOINT, credentials=credentials)

# Load image as binary
with open(IMAGE_PATH, "rb") as image_file:
    image_data = image_file.read()

# Make prediction
results = prediction_client.classify_image(PROJECT_ID, PUBLISHED_NAME, image_data)

# Open the image using PIL
image = Image.open(IMAGE_PATH).convert("RGB")
draw = ImageDraw.Draw(image)

# Load font (fallback to default)
try:
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()

# Handle prediction result
top_prediction = next((p for p in results.predictions if p.probability > 0.5), None)
if top_prediction:
    label = f"{top_prediction.tag_name} ({top_prediction.probability:.0%})"
else:
    label = "No prediction > 50% confidence"

# Draw label on image
draw.text((10, 10), label, fill=(0, 200, 0), font=font)

# Save output image
output_path = "data/predicted/pil_annotated.jpg"
image.save(output_path)

# Print the result to console
print(f"Prediction: {label}")
print(f"Labeled image saved at: {output_path}")
image.show()
