# randimggen

This adds a function that generates a random image using the Pillow library. The function takes in a width and a height, and generates an image with random pixel values.

To use the function, you will need to install the Pillow library by running 

> pip install pillow.

## Usage:
 from random_image_generator import generate_random_image

# Generate a random image with a width of 200 and a height of 100
  img = generate_random_image(200, 100)

 # Save the image to a file
 img.save('random.png')

# Implementation details:

The function generate_random_image uses the Image class from the Pillow library to create a new image with the specified dimensions. It then generates random values for the red, green, and blue channels of each pixel using the random module. The pixel data is then passed to the putdata method of the image to set the pixel values. Finally, the image object is returned.

## Testing:
I have added unit tests for the generate_random_image function to ensure that it is generating images correctly. The tests check that the function generates an image with the correct dimensions and that the pixel values are within the expected range.

Please let me know if you have any questions or if there is anything else I can do to improve this pull request.

