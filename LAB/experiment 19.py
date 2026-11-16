"""
EXPERIMENT 19
Aim: Implement the Erosion Morphological operations technique using OpenCV in Python.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded_image = cv2.erode(image, kernel, iterations=2)

cv2.imwrite("experiment 19_output.jpg", eroded_image)
print("[OK] Saved experiment 19_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Erosion Morphological Operation", eroded_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
