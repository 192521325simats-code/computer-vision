"""
EXPERIMENT 23
Aim: Implement the Top hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Top Hat (Difference between input image and Opening)
tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imwrite("experiment 23_output.jpg", tophat_image)
print("[OK] Saved experiment 23_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Morphological Operation", tophat_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
