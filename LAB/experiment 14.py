"""
EXPERIMENT 14
Aim: Perform Perspective Transformation on the given image using Python and OpenCV.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

rows, cols = image.shape[:2]

# Select 4 points from the original image
src_points = np.float32([
    [100, 100],
    [cols - 100, 100],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Select corresponding target points in destination image
dst_points = np.float32([
    [0, 0],
    [cols, 0],
    [120, rows],
    [cols - 120, rows]
])

# Compute 3x3 perspective transformation matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply warpPerspective
perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imwrite("experiment 14_output.jpg", perspective_image)
print("[OK] Saved experiment 14_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
