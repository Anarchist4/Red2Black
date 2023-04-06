import cv2
import numpy as np
from PIL import Image
from IPython.display import display

# Load the image
image = cv2.imread('img\baboon.png')
display(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))

result = image.copy()

# Define the lower boundary and upper boundary for red color in BGR format
lower_red = np.array([0, 0, 200])
upper_red = np.array([51, 87, 255]) ##exact color range of orange

# Create a binary mask based on the color range
mask = cv2.inRange(image, lower_red, upper_red)

# Set masked area to black pixels
result[mask==255] = [0, 0, 0]

# Convert the result image to uint8 data type
result = np.uint8(result)

display(Image.fromarray(cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)))
display(Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB)))
