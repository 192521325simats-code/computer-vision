"""
EXPERIMENT 23: Top Hat Morphological Operation

AIM:
    To implement the Top hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk.
    3. Define a 9x9 structuring element kernel.
    4. Apply Top Hat operation (difference between input image and opening) using cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel).
    5. Save the resulting Top Hat image using cv2.imwrite().
    6. Display original and Top Hat images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 23_output.jpg (Top hat filtered image)

RESULT:
    Thus, the top hat morphological operation was successfully implemented to isolate elements brighter than their surroundings.
"""

# ==================== PROGRAM CODE ====================
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

print("RESULT: Thus, the top hat morphological operation was successfully implemented to isolate elements brighter than their surroundings.")
