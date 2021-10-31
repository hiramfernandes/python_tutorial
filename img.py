# Open-CV Library for Python: https://pypi.org/project/opencv-python/
import cv2

# Transform existing images in arrays
im_g = cv2.imread("files/smallgray.png", 0)  # Zero stands for grayscale (1-dimension) arrays
print(im_g)

color_im_g = cv2.imread("files/smallgray.png", 1)  # Zero stands for RGB (3-dimension) arrays
print(color_im_g)

# Create images based on an existing array
cv2.imwrite("files/generatedsmallgray.png", im_g)

# Accessing subsets of an existing Numpy array (OpenCV)
out = im_g[0:2, 2:4] # Gets the first two rows and the second and third columns
print(out)
