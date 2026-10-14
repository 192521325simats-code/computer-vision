"""
EXPERIMENT 10
Aim: Perform a 90-degree rotation clockwise along the y-axis for the given image.
"""
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
