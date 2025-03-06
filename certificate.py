from PIL import Image, ImageDraw, ImageFont
import os

def generate_certificate(name):
    cert = Image.open("certificate.jpeg")
    draw = ImageDraw.Draw(cert)
    
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((550, 600), name, font=font, fill="black")

    directory = r"D:\imageprocessing"  # Use raw string to handle backslashes
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Use the full path when saving the file
    cert.save(os.path.join(directory, f"{name}.jpeg"))

generate_certificate("Subash  D")
