"""
EXPERIMENT 2: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to Blur using Gaussian Blur.

AIM:
    To perform basic image handling and processing operations by reading an image in Python and applying Gaussian Blur using OpenCV.

PROCEDURE:
    1. Import the OpenCV library (cv2).
    2. Read the input image from storage using cv2.imread().
    3. Apply Gaussian blur to the image using cv2.GaussianBlur() with kernel size (15, 15) and sigmaX=0.
    4. Save the blurred output image using cv2.imwrite().
    5. Display the original image and blurred image using cv2.imshow().
    6. Close all display windows after key press using cv2.destroyAllWindows().

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 2_output.jpg (Output image)

RESULT:
    Thus, Gaussian blur was successfully applied to the given image to achieve smoothing and noise reduction using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
if image is None:
    raise FileNotFoundError("Input image photo.jpg not found.")

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Save and display
cv2.imwrite("experiment 2_output.jpg", blurred)
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Gaussian blur complete.")

print("RESULT: Thus, Gaussian blur was successfully applied to the given image to achieve smoothing and noise reduction using OpenCV.")
