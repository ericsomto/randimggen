from PIL import Image, ImageDraw
import random

from random_art import run_expression

# Set the dimensions of the image
WIDTH = 640
HEIGHT = 480

# Create a blank image
img = Image.new('RGB', (WIDTH, HEIGHT))

# Create a drawing object
draw = ImageDraw.Draw(img)

# Generate a random color
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
def generate_monochrome_image(expression,
                              width=450,
                              height=450,
                              min_intensity=0,
                              max_intensity=255):
    def convert_coords(x, y):
        
        width_unit = width / 2
        height_unit = height / 2
        rx = (x - width_unit) / width_unit
        ry = (y - height_unit) / height_unit
        return (rx, ry)

    def scale_intensity(rel_intensity):
        multiplier = (max_intensity - min_intensity) / 2
        return int((rel_intensity + 1) * multiplier) + min_intensity

    image = Image.new("L", (width, height))
    for py in range(height):
        for px in range(width):
            x, y = convert_coords(px, py)
            expr_value = run_expression(expression, x, y)
            intensity = scale_intensity(expr_value)
            image.putpixel((px, py), intensity)

    return image

# Generate random coordinates for the top-left and bottom-right points of the rectangle
x1 = random.randint(0, WIDTH)
y1 = random.randint(0, HEIGHT)
x2 = random.randint(0, WIDTH)
y2 = random.randint(0, HEIGHT)

# Draw the rectangle on the image
draw.rectangle((x1, y1, x2, y2), fill=color)

# Save the image
img.save('killyourself.png')
