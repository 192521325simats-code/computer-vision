"""
EXPERIMENT 15: Perform Corner Detection using Harris Corner Detection Algorithm on the given image.

AIM:
    To detect and highlight corners in an image using the Harris Corner Detection algorithm in OpenCV.

PROCEDURE:
    1. Import cv2 and numpy.
    2. Read the image and convert it to grayscale.
    3. Convert the grayscale image to float32 data type.
    4. Apply Harris Corner Detection using cv2.cornerHarris().
    5. Dilate the detected corners for visual marking.
    6. Threshold corner responses and mark detected corner points in red on the original image.
    7. Save and display the corner-detected output.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 15_output.jpg (Output image)

RESULT:
    Thus, image corners were successfully detected and highlighted using the Harris Corner Detection algorithm in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris corner detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)
dst = cv2.dilate(dst, None)

# Mark corners in red
output = image.copy()
output[dst > 0.01 * dst.max()] = [0, 0, 255]

# Save and display
cv2.imwrite("experiment 15_output.jpg", output)
cv2.imshow("Harris Corners", output)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Harris corner detection complete.")

print("RESULT: Thus, image corners were successfully detected and highlighted using the Harris Corner Detection algorithm in OpenCV.")
