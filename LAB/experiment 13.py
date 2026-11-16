"""
EXPERIMENT 13: Affine Transformation

AIM:
    To perform Affine Transformation on a given image using Python and OpenCV by mapping 3 non-collinear reference points.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input image and obtain its dimensions (rows, cols).
    3. Define 3 non-collinear reference points in source and destination coordinates.
    4. Compute the 2x3 affine matrix using cv2.getAffineTransform(pts1, pts2).
    5. Apply affine transformation using cv2.warpAffine(image, M, (cols, rows)).
    6. Save and display the warped output image.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 13_output.jpg (Affine transformed image)

RESULT:
    Thus, affine transformation was successfully implemented on the given image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
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

print("RESULT: Thus, affine transformation was successfully implemented on the given image using OpenCV.")
