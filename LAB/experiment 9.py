"""
EXPERIMENT 9: Image Scaling Techniques (Upscaling and Downscaling)

AIM:
    To implement image scaling techniques to resize images to both bigger (upscaling) and smaller (downscaling) dimensions using OpenCV interpolation methods.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image and determine original width and height.
    3. Downscale image to 50% (0.5x) using cv2.resize() with cv2.INTER_AREA interpolation.
    4. Upscale image to 150% (1.5x) using cv2.resize() with cv2.INTER_CUBIC interpolation.
    5. Save both smaller and bigger resized images using cv2.imwrite().
    6. Display resized images and terminate windows.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 9_output.jpg, experiment 9_smaller.jpg, experiment 9_bigger.jpg

RESULT:
    Thus, image scaling techniques were successfully implemented to resize the given image to both smaller and bigger dimensions using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Downscale to smaller size (50%)
smaller = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Upscale to bigger size (150%)
bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imwrite("experiment 9_smaller.jpg", smaller)
cv2.imwrite("experiment 9_bigger.jpg", bigger)
cv2.imwrite("experiment 9_output.jpg", smaller)
print("[OK] Saved experiment 9_smaller.jpg, experiment 9_bigger.jpg, experiment 9_output.jpg")

cv2.imshow("Smaller Image (0.5x)", smaller)
cv2.imshow("Bigger Image (1.5x)", bigger)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, image scaling techniques were successfully implemented to resize the given image to both smaller and bigger dimensions using OpenCV.")
