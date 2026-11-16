"""
EXPERIMENT 6: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to erode using Erode function.

AIM:
    To perform morphological erosion on a given image using a structuring element kernel to diminish boundaries of foreground regions.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image using cv2.imread().
    3. Define a rectangular structuring element (kernel) using np.ones((5, 5), np.uint8).
    4. Apply morphological erosion using cv2.erode().
    5. Save the eroded output image using cv2.imwrite().
    6. Display the original image and the eroded image.
    7. Close all windows using cv2.destroyAllWindows().

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 6_output.jpg (Output image)

RESULT:
    Thus, morphological erosion was successfully applied to the image using the OpenCV cv2.erode function.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

# Perform erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Save and display
cv2.imwrite("experiment 6_output.jpg", eroded)
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Erosion operation complete.")

print("RESULT: Thus, morphological erosion was successfully applied to the image using the OpenCV cv2.erode function.")
