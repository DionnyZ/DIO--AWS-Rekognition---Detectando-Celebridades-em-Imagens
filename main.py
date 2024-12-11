import json
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

json_path = str(Path(__file__).parent / 'response.json')
print(json_path)
with open(json_path, 'r') as file:
    data = json.load(file)

image_path = str(Path(__file__).parent / 'images' / 'mercenarios.jpg')
image = Image.open(image_path)

draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 28)

for celebrity in data['CelebrityFaces']:
    name = celebrity['Name']
    box = celebrity['Face']['BoundingBox']
    
    width, height = image.size
    
    left = box['Left'] * width
    top = box['Top'] * height
    right = left + (box['Width'] * width)
    bottom = top + (box['Height'] * height)
    
    draw.rectangle([left, top, right, bottom], outline='red', width=3)
    
    draw.text((left, top - 40), name, fill='red', font=font)

output_path = os.path.join('images', 'mercenarios_recognized.jpg')
image.save(output_path)
