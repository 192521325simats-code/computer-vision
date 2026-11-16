"""
EXPERIMENT 8: Perform basic Image Handling and processing operations on the image is to read an image in python and Dilate an Image using Dilate function.

AIM:
    To perform morphological dilation on a given image using a structuring element kernel to expand foreground boundaries and fill small holes.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the input image using cv2.imread().
    3. Define a structuring element kernel of size 5x5 using np.ones().
    4. Apply morphological dilation using cv2.dilate().
    5. Save the dilated output image using cv2.imwrite().
    6. Display original and dilated images.
    7. Close all display windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 8_output.jpg (Output image)

RESULT:
    Thus, morphological dilation was successfully performed on the input image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)

# Perform dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Save and display
cv2.imwrite("experiment 8_output.jpg", dilated)
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Dilation operation complete.")

print("RESULT: Thus, morphological dilation was successfully performed on the input image using OpenCV.")
