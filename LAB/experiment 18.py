"""
EXPERIMENT 18: Image Cropping, Copying, and Pasting (Region of Interest - ROI)

AIM:
    To implement image cropping, copying, and pasting to select a region of interest (ROI) from the source image using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Read the input image and retrieve height and width.
    3. Define bounding coordinates (y1:y2, x1:x2) for the target ROI.
    4. Crop the Region of Interest using NumPy array slicing: roi = image[y1:y2, x1:x2].
    5. Paste the cropped ROI into another location in the image: output_image[y:y+h, x:x+w] = roi.
    6. Draw bounding indicator boxes around source and pasted ROI locations.
    7. Save the cropped ROI and final composite image.

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 18_output.jpg, experiment 18_cropped_roi.jpg

RESULT:
    Thus, image cropping, copying, and pasting of a Region of Interest (ROI) was successfully implemented using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

h, w = image.shape[:2]

# 1. Define ROI coordinates (e.g. center region / lighthouse tower)
y1, y2 = int(h * 0.3), int(h * 0.7)
x1, x2 = int(w * 0.35), int(w * 0.55)

# 2. Crop ROI
roi = image[y1:y2, x1:x2]
cv2.imwrite("experiment 18_cropped_roi.jpg", roi)

# 3. Copy and paste ROI into another region of the image
output_image = image.copy()
roi_h, roi_w = roi.shape[:2]

# Paste ROI at top-left
output_image[20:20 + roi_h, 20:20 + roi_w] = roi

# Draw bounding box on original location for visual reference
cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.putText(output_image, "Source ROI", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Draw bounding box on pasted location
cv2.rectangle(output_image, (20, 20), (20 + roi_w, 20 + roi_h), (0, 0, 255), 2)
cv2.putText(output_image, "Pasted ROI", (20, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

cv2.imwrite("experiment 18_output.jpg", output_image)
print("[OK] Saved experiment 18_output.jpg and experiment 18_cropped_roi.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("ROI Copy-Paste Result", output_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()

print("RESULT: Thus, image cropping, copying, and pasting of a Region of Interest (ROI) was successfully implemented using OpenCV.")
