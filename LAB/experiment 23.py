"""
EXPERIMENT 23: Implement the Top hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

AIM:
    To implement the Top Hat morphological filter (difference between input image and its opening) to isolate bright elements smaller than the structuring element.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Create a structuring element kernel of size 9x9.
    4. Execute Top Hat transformation using cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel).
    5. Save the Top Hat filtered image to disk.
    6. Display the output.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 23_output.jpg (Output image)

RESULT:
    Thus, the Top Hat morphological operation was successfully performed to extract prominent bright details using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

# Top Hat: Image minus Opening
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite("experiment 23_output.jpg", tophat)
print("Top Hat operation complete.")

print("RESULT: Thus, the Top Hat morphological operation was successfully performed to extract prominent bright details using OpenCV.")
