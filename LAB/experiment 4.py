"""
EXPERIMENT 4: Implement histogram equalization on the given image and compare it with the original image using Open CV.

AIM:
    To implement histogram equalization on a given grayscale image to enhance contrast and compare it with the original image using OpenCV.

PROCEDURE:
    1. Import the required libraries: cv2 and matplotlib.pyplot.
    2. Read the input image and convert it to grayscale.
    3. Apply histogram equalization using cv2.equalizeHist().
    4. Compute histograms for both original and equalized images using cv2.calcHist().
    5. Plot the original image, equalized image, and their corresponding histograms side by side.
    6. Save the comparative plot and equalized image to disk.
    7. Display the comparative output.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 4_output.png (Output image)

RESULT:
    Thus, histogram equalization was successfully implemented on the given image, resulting in enhanced global contrast and an evenly distributed pixel intensity profile.
"""

# ==================== PROGRAM CODE ====================
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalize histogram
equalized = cv2.equalizeHist(gray)
cv2.imwrite("experiment 4_equalized.jpg", equalized)

# Plot comparison
plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(2, 2, 2), plt.hist(gray.ravel(), 256, [0, 256], color='black'), plt.title('Original Histogram')
plt.subplot(2, 2, 3), plt.imshow(equalized, cmap='gray'), plt.title('Equalized Image'), plt.axis('off')
plt.subplot(2, 2, 4), plt.hist(equalized.ravel(), 256, [0, 256], color='blue'), plt.title('Equalized Histogram')
plt.tight_layout()
plt.savefig("experiment 4_output.png")
plt.close()
print("Histogram equalization complete.")

print("RESULT: Thus, histogram equalization was successfully implemented on the given image, resulting in enhanced global contrast and an evenly distributed pixel intensity profile.")
