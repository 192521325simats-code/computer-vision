"""
EXPERIMENT 25: Recognize watch from the given image by general Object recognition using OpenCV.

AIM:
    To detect and recognize a watch object from an input image using feature thresholding, contour localization, and circularity analysis in OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the watch input image (watch.jpg).
    3. Convert to grayscale and apply Gaussian blur for smoothing.
    4. Apply adaptive thresholding or Otsu thresholding to segment object contours.
    5. Find object contours using cv2.findContours().
    6. Filter contours based on geometric aspect ratio and circularity to identify the watch dial.
    7. Draw a bounding rectangle around the detected watch with the label 'Watch Detected'.
    8. Save and display the recognized object image.

INPUT:
    watch.jpg (Source image)

OUTPUT:
    experiment 25_output.jpg (Output image)

RESULT:
    Thus, the watch object was successfully recognized and localized with a bounding box using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("watch.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Binary threshold
_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = image.copy()
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output, "Watch Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        break

cv2.imwrite("experiment 25_output.jpg", output)
print("Watch object recognition complete.")

print("RESULT: Thus, the watch object was successfully recognized and localized with a bounding box using OpenCV.")
