"""
EXPERIMENT 1: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to Gray-scale.

AIM:
    To perform basic image handling and processing operations by reading an image in Python and converting the image into grayscale using OpenCV.

PROCEDURE:
    1. Install the OpenCV library using pip install opencv-python.
    2. Import the OpenCV library using import cv2.
    3. Read the input image using cv2.imread().
    4. Convert the color image into grayscale using cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).
    5. Save the grayscale image using cv2.imwrite().
    6. Display the original image and grayscale image using cv2.imshow().
    7. Wait for a key press using cv2.waitKey(0) and close all windows using cv2.destroyAllWindows().

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 1_output.jpg (Output image)

RESULT:
    Thus, the given image was successfully read using Python OpenCV and converted from a color image to a grayscale image.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

image = cv2.imread("photo.jpg")
if image is None:
    raise FileNotFoundError("Input image photo.jpg not found.")

# Convert color image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save and display
cv2.imwrite("experiment 1_output.jpg", gray)
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Grayscale conversion complete.")

print("RESULT: Thus, the given image was successfully read using Python OpenCV and converted from a color image to a grayscale image.")
