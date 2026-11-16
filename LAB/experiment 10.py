"""
EXPERIMENT 10: 90-Degree Clockwise Rotation along Y-Axis

AIM:
    To perform a 90-degree clockwise rotation and vertical/y-axis reflection for a given image using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image from disk using cv2.imread().
    3. Rotate the image 90 degrees clockwise using cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE).
    4. Apply horizontal flip along the y-axis using cv2.flip(image, 1).
    5. Save the rotated and flipped images using cv2.imwrite().
    6. Display output images and close windows.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 10_output.jpg (90-deg CW rotated), experiment 10_y_axis_flipped.jpg

RESULT:
    Thus, a 90-degree clockwise rotation and y-axis reflection were successfully performed on the given image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 90-degree clockwise rotation
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Flip along y-axis (horizontal mirror)
flipped_y = cv2.flip(image, 1)

cv2.imwrite("experiment 10_output.jpg", rotated_90)
cv2.imwrite("experiment 10_y_axis_flipped.jpg", flipped_y)
print("[OK] Saved experiment 10_output.jpg and experiment 10_y_axis_flipped.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("90 Degree Clockwise Rotation", rotated_90)
cv2.imshow("Flipped along Y-Axis", flipped_y)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, a 90-degree clockwise rotation and y-axis reflection were successfully performed on the given image using OpenCV.")
