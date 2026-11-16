"""
EXPERIMENT 1: Basic Image Handling and Grayscale Conversion

AIM:
    To perform basic image handling and processing operations by reading an image in Python and converting the image into grayscale using OpenCV.

PROCEDURE:
    1. Install the OpenCV library using pip install opencv-python.
    2. Import the OpenCV library using import cv2.
    3. Read the input image using cv2.imread().
    4. Convert the color image into grayscale using cv2.cvtColor().
    5. Save the grayscale image using cv2.imwrite().
    6. Display the original image and grayscale image using cv2.imshow().
    7. Wait for a key press using cv2.waitKey(0) and close all windows using cv2.destroyAllWindows().

INPUT:
    photo.jpg (RGB/BGR color image)

OUTPUT:
    experiment 1_output.jpg (Grayscale image)

RESULT:
    Thus, the given image was successfully read using Python OpenCV and converted from a color image to a grayscale image.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save output
cv2.imwrite("experiment 1_output.jpg", gray)
print("[OK] Saved experiment 1_output.jpg")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the given image was successfully read using Python OpenCV and converted from a color image to a grayscale image.")
