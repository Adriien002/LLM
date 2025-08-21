import base64
from PIL import Image
from io import BytesIO
import json

# Charge le JSON des images 
with open("/home/tibia/Documents/LLM/BrainGPT/data/CQ500p.json", "rb") as f:
    images = json.load(f)

# Test sur une image précise
image_id = 'ID_441cea72_ID_4b13324a92.nii_slice00' 
cur_image = images[image_id]

try:
    decoded = base64.urlsafe_b64decode(cur_image)
    img = Image.open(BytesIO(decoded)).convert("RGB")
    print(f"Image {image_id} loaded successfully, size: {img.size}")
except Exception as e:
    print(f"Error loading image {image_id}: {e}")