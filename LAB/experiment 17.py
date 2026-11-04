"""
EXPERIMENT 17
Aim: Implementation of Image Watermarking Technique using OpenCV.
"""
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

h, w = image.shape[:2]

# Create watermark image or load if exists
watermark_path = "watermark.jpg"
if os.path.exists(watermark_path):
    watermark = cv2.imread(watermark_path)
    watermark = cv2.resize(watermark, (w, h))
else:
    # Generate watermark image
    watermark = np.zeros_like(image)
    cv2.putText(watermark, "SIMATS CV LAB", (w // 8, h // 2),
                cv2.FONT_HERSHEY_DUPLEX, 2.5, (255, 255, 255), 6, cv2.LINE_AA)
    cv2.imwrite("watermark.jpg", watermark)

# Blend images to apply translucent watermark
watermarked_image = cv2.addWeighted(image, 0.8, watermark, 0.35, 0)

# Add visible watermark text banner at bottom
cv2.putText(watermarked_image, "CONFIDENTIAL - SIMATS", (30, h - 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)

cv2.imwrite("experiment 17_output.jpg", watermarked_image)
print("[OK] Saved experiment 17_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", watermarked_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
