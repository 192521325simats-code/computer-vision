"""
EXPERIMENT 11: 180-Degree Clockwise Rotation along Y-Axis

AIM:
    To perform a 180-degree clockwise rotation for a given image using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image from disk using cv2.imread().
    3. Rotate the image 180 degrees using cv2.rotate(image, cv2.ROTATE_180).
    4. Save the 180-degree rotated output image using cv2.imwrite().
    5. Display original and rotated images using cv2.imshow().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 11_output.jpg (180-degree rotated image)

RESULT:
    Thus, a 180-degree clockwise rotation was successfully performed on the given image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 180-degree rotation
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imwrite("experiment 11_output.jpg", rotated_180)
print("[OK] Saved experiment 11_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotation", rotated_180)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, a 180-degree clockwise rotation was successfully performed on the given image using OpenCV.")
