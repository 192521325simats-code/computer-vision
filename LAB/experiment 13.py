"""
EXPERIMENT 13: Perform Affine Transformation on the given image using python and Open CV.

AIM:
    To perform an Affine Transformation on an image using three non-collinear reference points to achieve shearing, translation, and scaling.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Define three source points on the original image.
    4. Define three corresponding destination points.
    5. Compute the 2x3 affine transformation matrix using cv2.getAffineTransform().
    6. Apply affine warp using cv2.warpAffine().
    7. Save and display the affine transformed image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 13_output.jpg (Output image)

RESULT:
    Thus, affine transformation was successfully implemented on the image using cv2.getAffineTransform and cv2.warpAffine in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
rows, cols = image.shape[:2]

# Define 3 source and destination points
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)
affine_result = cv2.warpAffine(image, matrix, (cols, rows))

# Save and display
cv2.imwrite("experiment 13_output.jpg", affine_result)
cv2.imshow("Affine Transformed", affine_result)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Affine transformation complete.")

print("RESULT: Thus, affine transformation was successfully implemented on the image using cv2.getAffineTransform and cv2.warpAffine in OpenCV.")
