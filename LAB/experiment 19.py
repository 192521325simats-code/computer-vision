"""
EXPERIMENT 19: Implement the Erosion Morphological operations technique using OpenCV in Python.

AIM:
    To implement morphological erosion to strip foreground pixel layers and shrink object boundaries using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Create an elliptical or rectangular structuring element kernel.
    4. Apply cv2.erode() with kernel size (5, 5).
    5. Save and display the eroded image.
    6. Close all display windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 19_output.jpg (Output image)

RESULT:
    Thus, morphological erosion was successfully implemented on the image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

eroded = cv2.erode(image, kernel, iterations=2)
cv2.imwrite("experiment 19_output.jpg", eroded)
print("Erosion morphological operation complete.")

print("RESULT: Thus, morphological erosion was successfully implemented on the image using OpenCV.")
