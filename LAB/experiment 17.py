"""
EXPERIMENT 17: Implement Image Watermarking technique using OpenCV in Python.

AIM:
    To implement an image watermarking technique by blending a logo/watermark onto a host image using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Read the source image (photo.jpg) and watermark image (watermark.jpg).
    3. Resize the watermark image to fit an appropriate region of the host image.
    4. Extract the Region of Interest (ROI) from the host image.
    5. Blend the ROI and the watermark using cv2.addWeighted() with specified alpha and beta transparency weights.
    6. Insert the blended watermark back into the host image.
    7. Save and display the watermarked image.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 17_output.jpg (Output image)

RESULT:
    Thus, the image watermarking technique was successfully implemented by seamlessly blending a watermark onto the host image using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("photo.jpg")
watermark = cv2.imread("watermark.jpg")

h_img, w_img = image.shape[:2]
wm_w = int(w_img * 0.25)
wm_h = int(h_img * 0.15)
watermark = cv2.resize(watermark, (wm_w, wm_h))

# Position watermark at bottom-right corner
x_offset = w_img - wm_w - 20
y_offset = h_img - wm_h - 20
roi = image[y_offset:y_offset + wm_h, x_offset:x_offset + wm_w]

# Blend images
blended = cv2.addWeighted(roi, 0.6, watermark, 0.4, 0)
image[y_offset:y_offset + wm_h, x_offset:x_offset + wm_w] = blended

cv2.imwrite("experiment 17_output.jpg", image)
print("Image watermarking complete.")

print("RESULT: Thus, the image watermarking technique was successfully implemented by seamlessly blending a watermark onto the host image using OpenCV.")
