"""
EXPERIMENT 15: Corner Detection using Harris Corner Detection Algorithm

AIM:
    To implement corner detection using the Harris Corner Detection algorithm in OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image and convert to grayscale.
    3. Cast the grayscale image array to float32.
    4. Apply Harris corner detection using cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04).
    5. Dilate detected corner points for enhanced visualization.
    6. Mark corner coordinates in red ([0, 0, 255]) on the output image.
    7. Save and display the corner-detected output image.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 15_output.jpg (Corner marked image)

RESULT:
    Thus, corners were successfully detected and localized in the given image using the Harris Corner Detection algorithm.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert image to grayscale and float32
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_float = np.float32(gray)

# Apply Harris Corner Detector
dst = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

# Dilate corner marks for better visibility
dst_dilated = cv2.dilate(dst, None)

# Create output image with red markings on corners
corner_image = image.copy()
corner_image[dst_dilated > 0.01 * dst_dilated.max()] = [0, 0, 255]

cv2.imwrite("experiment 15_output.jpg", corner_image)
print("[OK] Saved experiment 15_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", corner_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, corners were successfully detected and localized in the given image using the Harris Corner Detection algorithm.")
