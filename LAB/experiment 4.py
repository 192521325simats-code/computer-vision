"""
EXPERIMENT 4
Aim: Implement histogram equalization on the given image and compare it with the original image using OpenCV.
"""
import cv2
import matplotlib.pyplot as plt
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
cv2.imwrite("experiment 4_equalized.jpg", equalized)

# Compute histograms
hist_orig = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_eq = cv2.calcHist([equalized], [0], None, [256], [0, 256])

# Plotting and comparison
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1); plt.imshow(gray, cmap='gray'); plt.title("Original Grayscale")
plt.subplot(2, 2, 2); plt.plot(hist_orig, color='black'); plt.title("Original Histogram")
plt.subplot(2, 2, 3); plt.imshow(equalized, cmap='gray'); plt.title("Equalized Image")
plt.subplot(2, 2, 4); plt.plot(hist_eq, color='navy'); plt.title("Equalized Histogram")
plt.tight_layout()
plt.savefig("experiment 4_output.png")
print("[OK] Saved experiment 4_output.png")
plt.close()
