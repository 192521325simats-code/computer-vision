"""
EXPERIMENT 16: Implementation of Sobel Edge Detection Algorithm

AIM:
    To implement the Sobel Edge Detection algorithm in Python using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image and convert to grayscale.
    3. Calculate gradient in horizontal X-direction using cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3).
    4. Calculate gradient in vertical Y-direction using cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3).
    5. Convert gradient matrices to 8-bit unsigned values using cv2.convertScaleAbs().
    6. Blend horizontal and vertical edge maps using cv2.addWeighted().
    7. Save and display the directional and combined Sobel edge images.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 16_output.jpg, experiment 16_sobel_x.jpg, experiment 16_sobel_y.jpg

RESULT:
    Thus, the Sobel edge detection algorithm was successfully implemented to detect horizontal, vertical, and combined edges.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter in X and Y directions
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert back to 8-bit absolute values
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine Sobel X and Sobel Y
sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

cv2.imwrite("experiment 16_sobel_x.jpg", abs_sobel_x)
cv2.imwrite("experiment 16_sobel_y.jpg", abs_sobel_y)
cv2.imwrite("experiment 16_output.jpg", sobel_combined)
print("[OK] Saved experiment 16_output.jpg")

cv2.imshow("Sobel X", abs_sobel_x)
cv2.imshow("Sobel Y", abs_sobel_y)
cv2.imshow("Sobel Edge Detection", sobel_combined)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, the Sobel edge detection algorithm was successfully implemented to detect horizontal, vertical, and combined edges.")
