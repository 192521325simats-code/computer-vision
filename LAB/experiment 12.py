"""
EXPERIMENT 12
Aim: Perform a 270-degree rotation clockwise along the y-axis for the given image.
"""
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 270-degree clockwise rotation (equivalent to 90-degree counter-clockwise)
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("experiment 12_output.jpg", rotated_270)
print("[OK] Saved experiment 12_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("270 Degree Rotation", rotated_270)
cv2.waitKey(1000)
cv2.destroyAllWindows()
