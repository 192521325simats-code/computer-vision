"""
EXPERIMENT 14: Perform Perspective Transformation on the given image using python and Open CV.

AIM:
    To perform Perspective Transformation on an image using four reference points to change the viewing perspective (birds-eye view/homography).

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image.
    3. Define four source coordinates on the input plane.
    4. Define four destination coordinates on the target plane.
    5. Calculate the 3x3 perspective transformation matrix using cv2.getPerspectiveTransform().
    6. Apply the perspective warp using cv2.warpPerspective().
    7. Save and display the perspective transformed image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 14_output.jpg (Output image)

RESULT:
    Thus, perspective transformation was successfully performed on the image using OpenCV cv2.warpPerspective.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
h, w = image.shape[:2]

# Define 4 corner source points and destination points
pts1 = np.float32([[100, 100], [w - 100, 80], [80, h - 80], [w - 80, h - 100]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_result = cv2.warpPerspective(image, matrix, (w, h))

# Save and display
cv2.imwrite("experiment 14_output.jpg", perspective_result)
cv2.imshow("Perspective Transformed", perspective_result)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Perspective transformation complete.")

print("RESULT: Thus, perspective transformation was successfully performed on the image using OpenCV cv2.warpPerspective.")
