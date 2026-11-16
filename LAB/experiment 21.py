"""
EXPERIMENT 21: Opening Morphological Operation

AIM:
    To implement the Opening technique as a Morphological operation to dilate the foreground regions based on OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk.
    3. Define a 5x5 rectangular structuring element kernel.
    4. Apply morphological opening (erosion followed by dilation) using cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel).
    5. Save the resulting opened image using cv2.imwrite().
    6. Display original and opened images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 21_output.jpg (Opened image)

RESULT:
    Thus, the opening morphological operation was successfully implemented to remove background noise and separate connected components.
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

# Apply Opening (Erosion followed by Dilation)
opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imwrite("experiment 21_output.jpg", opening_image)
print("[OK] Saved experiment 21_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Opening Morphological Operation", opening_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the opening morphological operation was successfully implemented to remove background noise and separate connected components.")
