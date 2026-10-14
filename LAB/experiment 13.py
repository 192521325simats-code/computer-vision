"""
EXPERIMENT 13
Aim: Perform Affine Transformation on the given image using python and OpenCV.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

rows, cols, ch = image.shape

# 3 non-collinear reference points in input and output
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute 2x3 affine matrix
M = cv2.getAffineTransform(pts1, pts2)

# Warp affine
affine_img = cv2.warpAffine(image, M, (cols, rows))

cv2.imwrite("experiment 13_output.jpg", affine_img)
print("[OK] Saved experiment 13_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
