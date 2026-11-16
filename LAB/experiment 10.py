"""
EXPERIMENT 10: Perform a 90-degree rotation clockwise along the y-axis for the given image.

AIM:
    To rotate the given image 90 degrees clockwise and apply a reflection/flip along the y-axis using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Read the input image from disk using cv2.imread().
    3. Rotate the image 90 degrees clockwise using cv2.rotate() with cv2.ROTATE_90_CLOCKWISE.
    4. Perform horizontal flip (along y-axis) using cv2.flip(rotated, 1).
    5. Save and display the rotated and flipped image.
    6. Close all display windows.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 10_output.jpg (Output image)

RESULT:
    Thus, a 90-degree clockwise rotation and y-axis flip were successfully executed on the image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")

# 90 degrees clockwise rotation
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("experiment 10_output.jpg", rotated_90)

# Flip along y-axis (horizontal flip)
flipped_y = cv2.flip(rotated_90, 1)
cv2.imwrite("experiment 10_y_axis_flipped.jpg", flipped_y)
print("90 degree rotation complete.")

print("RESULT: Thus, a 90-degree clockwise rotation and y-axis flip were successfully executed on the image using OpenCV.")
