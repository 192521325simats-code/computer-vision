"""
EXPERIMENT 12: Perform a 270-degree rotation clockwise along the y-axis for the given image.

AIM:
    To rotate the given image 270 degrees clockwise (equivalent to 90 degrees counter-clockwise) using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Read the input image using cv2.imread().
    3. Apply 270 degrees clockwise rotation using cv2.ROTATE_90_COUNTERCLOCKWISE.
    4. Save the output rotated image using cv2.imwrite().
    5. Display the original and rotated images.
    6. Close all display windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 12_output.jpg (Output image)

RESULT:
    Thus, 270-degree clockwise rotation of the image was successfully performed using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")

# 270 degrees clockwise is 90 degrees counter-clockwise
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Save and display
cv2.imwrite("experiment 12_output.jpg", rotated_270)
cv2.imshow("Original Image", image)
cv2.imshow("270 Degree Rotated", rotated_270)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("270 degree rotation complete.")

print("RESULT: Thus, 270-degree clockwise rotation of the image was successfully performed using OpenCV.")
