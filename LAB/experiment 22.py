"""
EXPERIMENT 22: Closing Morphological Operation

AIM:
    To implement the Closing technique as a Morphological operation to dilate the foreground regions based on OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk.
    3. Define a 5x5 structuring element kernel.
    4. Apply morphological closing (dilation followed by erosion) using cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel).
    5. Save the resulting closed image using cv2.imwrite().
    6. Display original and closed images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 22_output.jpg (Closed image)

RESULT:
    Thus, the closing morphological operation was successfully implemented to close small interior holes and bridge gaps.
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
kernel = np.ones((5, 5), np.uint8)

# Apply Closing (Dilation followed by Erosion)
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("experiment 22_output.jpg", closing_image)
print("[OK] Saved experiment 22_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Closing Morphological Operation", closing_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the closing morphological operation was successfully implemented to close small interior holes and bridge gaps.")
