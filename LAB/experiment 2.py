"""
EXPERIMENT 2
Aim: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to Blur using Gaussian Blur.
"""
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite("experiment 2_output.jpg", blurred)
print("[OK] Saved experiment 2_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred)
cv2.waitKey(1000)
cv2.destroyAllWindows()
