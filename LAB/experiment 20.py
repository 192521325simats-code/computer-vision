"""
EXPERIMENT 20: Dilation Morphological Operations Technique

AIM:
    To implement the Dilation technique as a Morphological operation to dilate foreground regions based on OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk using cv2.imread().
    3. Create a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
    4. Apply morphological dilation using cv2.dilate(image, kernel, iterations=2).
    5. Save the dilated output image using cv2.imwrite().
    6. Display original and dilated images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 20_output.jpg (Dilated image)

RESULT:
    Thus, the dilation morphological operation was successfully implemented to expand foreground boundaries and fill gaps.
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

# Apply Dilation
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imwrite("experiment 20_output.jpg", dilated_image)
print("[OK] Saved experiment 20_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Dilation Morphological Operation", dilated_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the dilation morphological operation was successfully implemented to expand foreground boundaries and fill gaps.")
