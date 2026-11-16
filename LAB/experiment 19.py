"""
EXPERIMENT 19: Erosion Morphological Operations Technique

AIM:
    To implement the Erosion Morphological operations technique using OpenCV in Python.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image from disk using cv2.imread().
    3. Create a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
    4. Apply morphological erosion using cv2.erode(image, kernel, iterations=2).
    5. Save the eroded output image using cv2.imwrite().
    6. Display original and eroded images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 19_output.jpg (Eroded image)

RESULT:
    Thus, the erosion morphological operation was successfully implemented to thin foreground boundaries and reduce noise.
"""

# ==================== PROGRAM CODE ====================
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

print("RESULT: Thus, the erosion morphological operation was successfully implemented to thin foreground boundaries and reduce noise.")
