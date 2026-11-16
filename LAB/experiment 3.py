"""
EXPERIMENT 3: Perform basic Image Handling and processing operations on the image is to read an image in python and Convert an Image to show outline using Canny function.

AIM:
    To perform basic image handling and processing operations by reading an image in Python and extracting edge outlines using the Canny edge detector function.

PROCEDURE:
    1. Import the OpenCV library (cv2).
    2. Read the input image using cv2.imread().
    3. Convert the color image to grayscale using cv2.cvtColor().
    4. Apply Canny edge detection using cv2.Canny() with lower threshold 100 and upper threshold 200.
    5. Save the edge outline image using cv2.imwrite().
    6. Display the original image and outline image using cv2.imshow().
    7. Close all windows using cv2.destroyAllWindows().

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 3_output.jpg (Output image)

RESULT:
    Thus, outline edges of the given image were successfully extracted and displayed using the Canny edge detection function in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
if image is None:
    raise FileNotFoundError("Input image photo.jpg not found.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Save and display
cv2.imwrite("experiment 3_output.jpg", edges)
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edges Outline", edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("Canny outline detection complete.")

print("RESULT: Thus, outline edges of the given image were successfully extracted and displayed using the Canny edge detection function in OpenCV.")
