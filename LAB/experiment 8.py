"""
EXPERIMENT 8: Morphological Dilation using Dilate Function

AIM:
    To perform basic image handling and processing operations by reading an image in Python and applying morphological dilation using OpenCV's dilate() function.

PROCEDURE:
    1. Import cv2, numpy, and os.
    2. Read the input image from storage using cv2.imread().
    3. Define a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
    4. Apply morphological dilation using cv2.dilate(image, kernel, iterations=1).
    5. Save the dilated output image using cv2.imwrite().
    6. Display original and dilated images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 8_output.jpg (Dilated image)

RESULT:
    Thus, morphological dilation was successfully implemented on the image using OpenCV's dilate() function.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite("experiment 8_output.jpg", dilated)
print("[OK] Saved experiment 8_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, morphological dilation was successfully implemented on the image using OpenCV's dilate() function.")
