"""
EXPERIMENT 20
Aim: Implement the Dilation technique as a Morphological operation to dilate the foreground regions based on OpenCV.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Dilation
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imwrite("experiment 20_output.jpg", dilated_image)
print("[OK] Saved experiment 20_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Dilation Morphological Operation", dilated_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
