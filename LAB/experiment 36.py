"""
EXPERIMENT 36: Write a Python function to subtract the background of the given input image based on color levels using Open CV.

AIM:
    To perform background subtraction on an input image based on color level thresholding in the HSV color space using OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input color image.
    3. Convert the color space from BGR to HSV using cv2.cvtColor(image, cv2.COLOR_BGR2HSV).
    4. Determine the HSV color range representing the background (e.g. blue sky and cloud levels).
    5. Generate a binary background mask using cv2.inRange().
    6. Invert the mask using cv2.bitwise_not() to obtain the foreground mask.
    7. Apply cv2.bitwise_and() to isolate foreground objects with the background subtracted (blackened).
    8. Save and display the background-subtracted output image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 36_output.jpg (Output image)

RESULT:
    Thus, background subtraction based on color levels was successfully performed using HSV color thresholding in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV range for sky background
lower_sky = np.array([90, 20, 150])
upper_sky = np.array([130, 255, 255])

# Mask background and compute inverse for foreground
bg_mask = cv2.inRange(hsv, lower_sky, upper_sky)
fg_mask = cv2.bitwise_not(bg_mask)

# Subtract background
bg_subtracted = cv2.bitwise_and(image, image, mask=fg_mask)

# Save and display
cv2.imwrite("experiment 36_output.jpg", bg_subtracted)
cv2.imshow("Background Subtracted Image", bg_subtracted)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Background subtraction complete.")

print("RESULT: Thus, background subtraction based on color levels was successfully performed using HSV color thresholding in OpenCV.")
