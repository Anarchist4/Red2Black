## red 2 black pixels
import cv2
import numpy as np
from PIL import Image
# Load the image
im_path = "img\baboon.png"
im_bgr = cv2.imread(im_path)

# Convert the image to HSV color space
im_hsv = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2HSV)

# Define the lower and upper threshold for red color in HSV
lower_red = np.array([0,0,0])  # Hue range for red color in OpenCV is 0-180
upper_red = np.array([10, 255, 255])

# Apply the color threshold to get a binary mask
mask = cv2.inRange(im_hsv, lower_red, upper_red)

# Replace red pixels with black color in the original image
im_bgr[mask == 255] = [0, 0, 0]

#modified image with black colors
cv2.imshow("Modified Image", im_bgr)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
