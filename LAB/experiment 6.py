"""
EXPERIMENT 6: Morphological Erosion using Erode Function

AIM:
    To perform basic image handling and processing operations by reading an image in Python and applying morphological erosion using OpenCV's erode() function.

PROCEDURE:
    1. Import cv2, numpy, and os.
    2. Read the input image from disk using cv2.imread().
    3. Define a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
    4. Apply morphological erosion using cv2.erode(image, kernel, iterations=1).
    5. Save the eroded output image using cv2.imwrite().
    6. Display original and eroded images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 6_output.jpg (Eroded image)

RESULT:
    Thus, morphological erosion was successfully implemented on the image using OpenCV's erode() function.
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
eroded = cv2.erode(image, kernel, iterations=1)
cv2.imwrite("experiment 6_output.jpg", eroded)
print("[OK] Saved experiment 6_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, morphological erosion was successfully implemented on the image using OpenCV's erode() function.")
