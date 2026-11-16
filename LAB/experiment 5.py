"""
EXPERIMENT 5: Write a Python function to analyze the histogram of the given input image based on color levels using Open CV.

AIM:
    To analyze the color level distribution of an input image by calculating and plotting separate histograms for the Blue, Green, and Red color channels using OpenCV.

PROCEDURE:
    1. Import cv2, matplotlib.pyplot, and numpy.
    2. Read the input color image in BGR format.
    3. Split or iterate over individual color channels: Blue (0), Green (1), and Red (2).
    4. Calculate the histogram for each color channel using cv2.calcHist().
    5. Plot each channel's histogram using its corresponding curve color.
    6. Save and display the color histogram visualization.

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 5_output.png (Output image)

RESULT:
    Thus, the histogram of the input image based on Blue, Green, and Red color levels was successfully computed and plotted using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("photo.jpg")
colors = ('b', 'g', 'r')
channel_names = ('Blue Channel', 'Green Channel', 'Red Channel')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Input Image")
plt.axis("off")

plt.subplot(1, 2, 2)
for i, col in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=channel_names[i])
plt.title("Color Level Histogram Analysis")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("experiment 5_output.png")
plt.close()
print("Color histogram analysis complete.")

print("RESULT: Thus, the histogram of the input image based on Blue, Green, and Red color levels was successfully computed and plotted using OpenCV.")
