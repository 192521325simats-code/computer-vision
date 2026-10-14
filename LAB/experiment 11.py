"""
EXPERIMENT 11
Aim: Perform a 180-degree rotation clockwise along the y-axis for the given image.
"""
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
