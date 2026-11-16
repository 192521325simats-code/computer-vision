"""
EXPERIMENT 24: Implement the Black hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

AIM:
    To implement the Black Hat morphological filter (difference between closing and input image) to highlight dark features on a bright background.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Define a structuring element kernel of size 9x9.
    4. Apply Black Hat transformation using cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel).
    5. Save the output image.
    6. Display the result and close all windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 24_output.jpg (Output image)

RESULT:
    Thus, the Black Hat morphological operation was successfully implemented to isolate dark features using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

# Black Hat: Closing minus Image
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
cv2.imwrite("experiment 24_output.jpg", blackhat)
print("Black Hat operation complete.")

print("RESULT: Thus, the Black Hat morphological operation was successfully implemented to isolate dark features using OpenCV.")
