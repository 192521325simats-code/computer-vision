"""
EXPERIMENT 37: Write a Python function to subtract the foreground of the given input image based on color levels using Open CV.

AIM:
    To subtract the foreground objects from an input image based on color level thresholding in OpenCV, leaving the background intact.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input color image.
    3. Convert the image to HSV color space for robust color isolation.
    4. Define the color threshold range identifying the prominent foreground object colors.
    5. Create a foreground mask using cv2.inRange() and dilate slightly to ensure complete coverage.
    6. Compute the inverted mask representing purely background regions.
    7. Segment the background using cv2.bitwise_and(image, image, mask=background_mask) to subtract the foreground objects.
    8. Save and display the foreground-subtracted image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 37_output.jpg (Output image)

RESULT:
    Thus, foreground subtraction based on color levels was successfully implemented using OpenCV color thresholding.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Identify foreground colors (e.g. red/orange tones of tower and structures)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([15, 255, 255])
lower_red2 = np.array([165, 70, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
fg_mask = cv2.bitwise_or(mask1, mask2)
fg_mask = cv2.dilate(fg_mask, np.ones((5, 5), np.uint8), iterations=2)

# Invert mask to keep background only
bg_mask = cv2.bitwise_not(fg_mask)
fg_subtracted = cv2.bitwise_and(image, image, mask=bg_mask)

# Save and display
cv2.imwrite("experiment 37_output.jpg", fg_subtracted)
cv2.imshow("Foreground Subtracted Image", fg_subtracted)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Foreground subtraction complete.")

print("RESULT: Thus, foreground subtraction based on color levels was successfully implemented using OpenCV color thresholding.")
