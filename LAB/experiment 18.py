"""
EXPERIMENT 18: Implement image cropping, copying and pasting to select a region of interest (ROI) from the source image using OpenCV.

AIM:
    To select, crop, copy, and paste a Region of Interest (ROI) from a source image to another location within the image using NumPy slicing and OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Read the input image.
    3. Define bounding coordinates [y1:y2, x1:x2] for the Region of Interest (ROI).
    4. Crop the ROI using array slicing: roi = image[y1:y2, x1:x2].
    5. Save the cropped ROI to disk.
    6. Paste the copied ROI onto a new coordinate location within the image.
    7. Save and display the final composite output image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 18_output.jpg (Output image)

RESULT:
    Thus, image cropping, copying, and pasting of a Region of Interest (ROI) was successfully implemented using OpenCV array slicing.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
h, w = image.shape[:2]

# Define and crop ROI (lighthouse tower region)
roi = image[100:450, 350:550].copy()
cv2.imwrite("experiment 18_cropped_roi.jpg", roi)

# Paste cropped ROI to another area
output = image.copy()
roi_h, roi_w = roi.shape[:2]
output[100:100 + roi_h, 50:50 + roi_w] = roi

cv2.imwrite("experiment 18_output.jpg", output)
print("ROI cropping and pasting complete.")

print("RESULT: Thus, image cropping, copying, and pasting of a Region of Interest (ROI) was successfully implemented using OpenCV array slicing.")
