"""
EXPERIMENT 3: Outline and Edge Detection using Canny Function

AIM:
    To perform basic image handling and processing operations by reading an image in Python and extracting edge outlines using the Canny edge detector function.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image using cv2.imread().
    3. Convert the color image to grayscale using cv2.cvtColor().
    4. Apply Canny edge detection using cv2.Canny() with lower threshold 100 and upper threshold 200.
    5. Save the edge outline image using cv2.imwrite().
    6. Display the original image and outline image using cv2.imshow().
    7. Close all windows on key press using cv2.destroyAllWindows().

INPUT:
    photo.jpg (Input color image)

OUTPUT:
    experiment 3_output.jpg (Canny edge outline image)

RESULT:
    Thus, edge outlines were successfully extracted from the input image using the Canny edge detection function in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Save output
cv2.imwrite("experiment 3_output.jpg", edges)
print("[OK] Saved experiment 3_output.jpg")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Outline", edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, edge outlines were successfully extracted from the input image using the Canny edge detection function in OpenCV.")
