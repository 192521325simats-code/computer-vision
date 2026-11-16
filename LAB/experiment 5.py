"""
EXPERIMENT 5: Histogram Analysis Based on Color Levels

AIM:
    To write a Python function to analyze the histogram of the given input image based on color levels using OpenCV.

PROCEDURE:
    1. Import cv2, matplotlib.pyplot, and os.
    2. Define a function analyze_histogram(img_path).
    3. Read the input color image in BGR format.
    4. Iterate over each color channel (Blue, Green, Red) and calculate histograms using cv2.calcHist().
    5. Plot intensity curves for each color level on a single graph.
    6. Save the color histogram chart and display results.

INPUT:
    photo.jpg (Input color image)

OUTPUT:
    experiment 5_output.png (Color levels histogram chart)

RESULT:
    Thus, the histogram of the input image was successfully analyzed across individual color levels (Blue, Green, Red) using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2
import matplotlib.pyplot as plt
import os

def analyze_histogram(img_path):
    image = cv2.imread(img_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {img_path}")
    
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')
    
    plt.figure(figsize=(8, 5))
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=f"{channel_names[i]} Level")
        plt.xlim([0, 256])
        
    plt.title("Histogram Based on Color Levels")
    plt.xlabel("Color Levels (0 - 255)")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.grid(True)
    plt.savefig("experiment 5_output.png")
    print("[OK] Saved experiment 5_output.png")
    plt.close()

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
analyze_histogram(img_path)

print("RESULT: Thus, the histogram of the input image was successfully analyzed across individual color levels (Blue, Green, Red) using OpenCV.")
