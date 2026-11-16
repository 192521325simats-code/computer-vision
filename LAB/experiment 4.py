"""
EXPERIMENT 4: Histogram Equalization on Given Image and Comparison

AIM:
    To implement histogram equalization on a given image and compare it with the original image using OpenCV.

PROCEDURE:
    1. Import cv2, matplotlib.pyplot, and os.
    2. Read the input image and convert it to grayscale.
    3. Equalize the grayscale image histogram using cv2.equalizeHist().
    4. Compute histograms for both original and equalized images using cv2.calcHist().
    5. Plot comparative graphs showing original vs equalized images and their intensity histograms.
    6. Save the plot to disk using plt.savefig().

INPUT:
    photo.jpg (Input image)

OUTPUT:
    experiment 4_output.png (Comparative plot), experiment 4_equalized.jpg

RESULT:
    Thus, histogram equalization was successfully implemented on the given image, enhancing contrast and balancing pixel distribution.
"""

# ==================== PROGRAM CODE ====================
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
print("[OK] Saved experiment 4_output.png and experiment 4_equalized.jpg")
plt.close()

print("RESULT: Thus, histogram equalization was successfully implemented on the given image, enhancing contrast and balancing pixel distribution.")
