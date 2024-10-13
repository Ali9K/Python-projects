from PIL import Image, ImageDraw, ImageFont

image = Image.open('your_image_file.jpg')

if image.mode != 'RGB':
      image = image.convert('RGB')

draw = ImageDraw.Draw(image)
text = "Converted by Ali"
try:
      font = ImageFont.truetype("arial.ttf", 150)
except IOError:
      font = ImageFont.load_default()
x1, y1 = image.size
bbox = draw.textbbox((0,0) , text, font= font)
x2 = bbox[2] - bbox[0]
y2 = bbox[3] - bbox[1]
position = (x1 - x2, y1 - y2)

draw.text(position, text, (255,0,0), font = font)

image.save('output_file.pdf')

print("Your image has been converted to PDF successfully.")
