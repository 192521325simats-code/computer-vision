"""
EXPERIMENT 20: Implement the Dilation technique as a Morphological operation to dilate the foreground regions based on OpenCV.

AIM:
    To implement morphological dilation to expand foreground boundaries and bridge broken components using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Construct a 5x5 structuring element kernel using np.ones().
    4. Apply morphological dilation using cv2.dilate().
    5. Save the dilated image and display the result.
    6. Close all active windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 20_output.jpg (Output image)

RESULT:
    Thus, morphological dilation was successfully implemented to dilate foreground regions using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

dilated = cv2.dilate(image, kernel, iterations=2)
cv2.imwrite("experiment 20_output.jpg", dilated)
print("Dilation morphological operation complete.")

print("RESULT: Thus, morphological dilation was successfully implemented to dilate foreground regions using OpenCV.")
