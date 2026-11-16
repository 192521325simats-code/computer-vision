"""
EXPERIMENT 22: Implement the Closing technique as a Morphological operation to dilate the foreground regions based on OpenCV.

AIM:
    To implement Morphological Closing (dilation followed by erosion) to fill interior holes and bridge small gaps in the image using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Define a 5x5 structuring element kernel.
    4. Apply morphological closing using cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel).
    5. Save the closed output image.
    6. Display the result and terminate cleanly.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 22_output.jpg (Output image)

RESULT:
    Thus, morphological closing was successfully implemented to close small gaps and holes using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

# Morphological Closing: Dilation followed by Erosion
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("experiment 22_output.jpg", closed)
print("Closing morphological operation complete.")

print("RESULT: Thus, morphological closing was successfully implemented to close small gaps and holes using OpenCV.")
