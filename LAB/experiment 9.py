"""
EXPERIMENT 9: Implement the image scaling techniques to resize the images to both bigger and small sizes.

AIM:
    To implement image scaling techniques to resize an image into both enlarged (upscaled) and reduced (downscaled) dimensions using OpenCV.

PROCEDURE:
    1. Import the OpenCV library (cv2).
    2. Read the input image from disk.
    3. Scale the image to a smaller size using cv2.resize() with INTER_AREA interpolation.
    4. Scale the image to a larger size using cv2.resize() with INTER_CUBIC interpolation.
    5. Save both scaled images to disk.
    6. Display original, downscaled, and upscaled images.
    7. Close all active windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 9_output.jpg (Output image)

RESULT:
    Thus, image scaling techniques to resize images to both smaller and larger sizes were successfully implemented using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
h, w = image.shape[:2]

# Scale smaller (0.5x)
smaller = cv2.resize(image, (int(w * 0.5), int(h * 0.5)), interpolation=cv2.INTER_AREA)
cv2.imwrite("experiment 9_smaller.jpg", smaller)

# Scale bigger (1.5x)
bigger = cv2.resize(image, (int(w * 1.5), int(h * 1.5)), interpolation=cv2.INTER_CUBIC)
cv2.imwrite("experiment 9_bigger.jpg", bigger)

# Primary output
cv2.imwrite("experiment 9_output.jpg", bigger)
print("Image scaling complete.")

print("RESULT: Thus, image scaling techniques to resize images to both smaller and larger sizes were successfully implemented using OpenCV.")
