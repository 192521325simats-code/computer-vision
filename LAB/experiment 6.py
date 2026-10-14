"""
EXPERIMENT 6
Aim: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to erode using Erode function.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)
cv2.imwrite("experiment 6_output.jpg", eroded)
print("[OK] Saved experiment 6_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(1000)
cv2.destroyAllWindows()
