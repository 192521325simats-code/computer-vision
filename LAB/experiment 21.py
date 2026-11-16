"""
EXPERIMENT 21: Implement the Opening technique as a Morphological operation to dilate the foreground regions based on OpenCV.

AIM:
    To implement Morphological Opening (erosion followed by dilation) to remove isolated background noise and smooth object contours using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Define a structuring element kernel of size 5x5.
    4. Execute morphological opening using cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel).
    5. Save the opened output image.
    6. Display the result and close all windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 21_output.jpg (Output image)

RESULT:
    Thus, morphological opening was successfully implemented to remove background noise while preserving foreground features using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

# Morphological Opening: Erosion followed by Dilation
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
cv2.imwrite("experiment 21_output.jpg", opened)
print("Opening morphological operation complete.")

print("RESULT: Thus, morphological opening was successfully implemented to remove background noise while preserving foreground features using OpenCV.")
