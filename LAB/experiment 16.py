"""
EXPERIMENT 16: Implement the Sobel Edge Detection Algorithm to find edges in both horizontal and vertical directions.

AIM:
    To perform Sobel edge detection to compute horizontal, vertical, and combined edge gradients in an image using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image and convert it to grayscale.
    3. Compute the horizontal gradient (Sobel X) using cv2.Sobel(gray, cv2.CV_64F, 1, 0).
    4. Compute the vertical gradient (Sobel Y) using cv2.Sobel(gray, cv2.CV_64F, 0, 1).
    5. Calculate gradient magnitude using cv2.magnitude().
    6. Convert gradients to 8-bit unsigned integers using cv2.convertScaleAbs().
    7. Save the Sobel X, Sobel Y, and combined edge images to disk.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 16_output.jpg (Output image)

RESULT:
    Thus, edge detection in horizontal and vertical directions was successfully implemented using the Sobel operator in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate Sobel in X and Y
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

abs_x = cv2.convertScaleAbs(sobel_x)
abs_y = cv2.convertScaleAbs(sobel_y)
sobel_combined = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

cv2.imwrite("experiment 16_sobel_x.jpg", abs_x)
cv2.imwrite("experiment 16_sobel_y.jpg", abs_y)
cv2.imwrite("experiment 16_output.jpg", sobel_combined)
print("Sobel edge detection complete.")

print("RESULT: Thus, edge detection in horizontal and vertical directions was successfully implemented using the Sobel operator in OpenCV.")
