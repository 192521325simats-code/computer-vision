"""
EXPERIMENT 11: Perform a 180-degree rotation clockwise along the y-axis for the given image.

AIM:
    To rotate the given image 180 degrees clockwise using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Read the input image from disk.
    3. Rotate the image 180 degrees using cv2.rotate() with cv2.ROTATE_180.
    4. Save the transformed image to disk using cv2.imwrite().
    5. Display the original and 180-degree rotated images.
    6. Close all windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 11_output.jpg (Output image)

RESULT:
    Thus, the given image was successfully rotated 180 degrees clockwise using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")

# 180 degrees rotation
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)

# Save and display
cv2.imwrite("experiment 11_output.jpg", rotated_180)
cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotated", rotated_180)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print("180 degree rotation complete.")

print("RESULT: Thus, the given image was successfully rotated 180 degrees clockwise using OpenCV.")
