"""
EXPERIMENT 9
Aim: Implement the image scaling techniques to resize the images to both bigger and small sizes.
"""
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
