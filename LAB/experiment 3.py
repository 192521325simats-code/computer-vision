"""
EXPERIMENT 3
Aim: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to show outline using Canny function.
"""
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("experiment 3_output.jpg", edges)
print("[OK] Saved experiment 3_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Canny Outline", edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()
