"""
EXPERIMENT 31: Implement a Segmentation algorithm using Open CV to segment the given input image based on the given threshold values.

AIM:
    To implement an image segmentation algorithm using OpenCV to segment foreground objects from the background based on threshold values.

PROCEDURE:
    1. Import cv2, numpy, and os.
    2. Read the input image using cv2.imread().
    3. Convert the image to grayscale using cv2.cvtColor().
    4. Apply Gaussian blurring to smooth the image and suppress noise.
    5. Apply Otsu thresholding using cv2.threshold() to segment the image automatically based on pixel intensity histogram.
    6. Apply bitwise AND operation (cv2.bitwise_and) using the threshold mask to extract the segmented foreground region.
    7. Save and display the segmented output image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 31_output.jpg (Output image)

RESULT:
    Thus, the image segmentation algorithm based on threshold values was successfully implemented using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

# Read input image
image = cv2.imread("photo.jpg")
if image is None:
    raise FileNotFoundError("Input image photo.jpg not found.")

# Convert to grayscale and blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold segmentation (Otsu thresholding)
_, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Segment foreground using bitwise AND
segmented = cv2.bitwise_and(image, image, mask=thresh)

# Save and display
cv2.imwrite("experiment 31_output.jpg", segmented)
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Output", segmented)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Threshold segmentation complete.")

print("RESULT: Thus, the image segmentation algorithm based on threshold values was successfully implemented using OpenCV.")
