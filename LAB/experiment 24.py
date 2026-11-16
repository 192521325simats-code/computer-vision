"""
EXPERIMENT 24: Black Hat Morphological Operation

AIM:
    To implement the Black hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk.
    3. Define a 9x9 structuring element kernel.
    4. Apply Black Hat operation (difference between closing and input image) using cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel).
    5. Save the resulting Black Hat image using cv2.imwrite().
    6. Display original and Black Hat images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 24_output.jpg (Black hat filtered image)

RESULT:
    Thus, the black hat morphological operation was successfully implemented to isolate elements darker than their surroundings.
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

# Apply Black Hat (Difference between Closing and input image)
blackhat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite("experiment 24_output.jpg", blackhat_image)
print("[OK] Saved experiment 24_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Morphological Operation", blackhat_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the black hat morphological operation was successfully implemented to isolate elements darker than their surroundings.")
