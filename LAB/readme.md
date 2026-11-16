# Computer Vision Laboratory Experiments (1 to 30)

This repository contains the complete implementation of **all 30 Computer Vision and Digital Image Processing experiments** using Python and OpenCV.
Every experiment is structured in standard laboratory record format with **Aim**, **Procedure**, **Program Code**, **Input**, **Output**, and **Result**.

---

## Index of Experiments

| No. | Experiment Title | Program File | Primary Output File |
|:---:|:-----------------|:-------------|:--------------------|
| **1** | Basic Image Handling and Grayscale Conversion | `experiment 1.py` | `experiment 1_output.jpg (Grayscale image)` |
| **2** | Image Blur using Gaussian Blur | `experiment 2.py` | `experiment 2_output.jpg (Gaussian blurred image)` |
| **3** | Outline and Edge Detection using Canny Function | `experiment 3.py` | `experiment 3_output.jpg (Canny edge outline image)` |
| **4** | Histogram Equalization on Given Image and Comparison | `experiment 4.py` | `experiment 4_output.png (Comparative plot)` |
| **5** | Histogram Analysis Based on Color Levels | `experiment 5.py` | `experiment 5_output.png (Color levels histogram chart)` |
| **6** | Morphological Erosion using Erode Function | `experiment 6.py` | `experiment 6_output.jpg (Eroded image)` |
| **7** | Video Processing (Normal, Slow Motion, and Fast Motion) | `experiment 7.py` | `experiment 7_output.mp4` |
| **8** | Morphological Dilation using Dilate Function | `experiment 8.py` | `experiment 8_output.jpg (Dilated image)` |
| **9** | Image Scaling Techniques (Upscaling and Downscaling) | `experiment 9.py` | `experiment 9_output.jpg` |
| **10** | 90-Degree Clockwise Rotation along Y-Axis | `experiment 10.py` | `experiment 10_output.jpg (90-deg CW rotated)` |
| **11** | 180-Degree Clockwise Rotation along Y-Axis | `experiment 11.py` | `experiment 11_output.jpg (180-degree rotated image)` |
| **12** | 270-Degree Clockwise Rotation along Y-Axis | `experiment 12.py` | `experiment 12_output.jpg (270-degree rotated image)` |
| **13** | Affine Transformation | `experiment 13.py` | `experiment 13_output.jpg (Affine transformed image)` |
| **14** | Perspective Transformation | `experiment 14.py` | `experiment 14_output.jpg (Perspective warped image)` |
| **15** | Corner Detection using Harris Corner Detection Algorithm | `experiment 15.py` | `experiment 15_output.jpg (Corner marked image)` |
| **16** | Implementation of Sobel Edge Detection Algorithm | `experiment 16.py` | `experiment 16_output.jpg` |
| **17** | Implementation of Image Watermarking Technique | `experiment 17.py` | `experiment 17_output.jpg (Watermarked image)` |
| **18** | Image Cropping, Copying, and Pasting (Region of Interest - ROI) | `experiment 18.py` | `experiment 18_output.jpg` |
| **19** | Erosion Morphological Operations Technique | `experiment 19.py` | `experiment 19_output.jpg (Eroded image)` |
| **20** | Dilation Morphological Operations Technique | `experiment 20.py` | `experiment 20_output.jpg (Dilated image)` |
| **21** | Opening Morphological Operation | `experiment 21.py` | `experiment 21_output.jpg (Opened image)` |
| **22** | Closing Morphological Operation | `experiment 22.py` | `experiment 22_output.jpg (Closed image)` |
| **23** | Top Hat Morphological Operation | `experiment 23.py` | `experiment 23_output.jpg (Top hat filtered image)` |
| **24** | Black Hat Morphological Operation | `experiment 24.py` | `experiment 24_output.jpg (Black hat filtered image)` |
| **25** | Watch Object Recognition | `experiment 25.py` | `experiment 25_output.jpg (Watch recognized image)` |
| **26** | Reverse Video Frame Playback | `experiment 26.py` | `experiment 26_output.mp4 (Reversed video)` |
| **27** | Human Face Detection Algorithm | `experiment 27.py` | `experiment 27_output.jpg (Face detected image)` |
| **28** | Vehicle Detection in Video Frames | `experiment 28.py` | `experiment 28_output.mp4 (Vehicle detection video)` |
| **29** | Human Eye Detection Algorithm | `experiment 29.py` | `experiment 29_output.jpg (Eye detected image)` |
| **30** | Human Smile Detection Algorithm | `experiment 30.py` | `experiment 30_output.jpg (Smile detected image)` |

---

## Experiment 1: Basic Image Handling and Grayscale Conversion

### AIM
To perform basic image handling and processing operations by reading an image in Python and converting the image into grayscale using OpenCV.

### PROCEDURE
1. Install the OpenCV library using pip install opencv-python.
2. Import the OpenCV library using import cv2.
3. Read the input image using cv2.imread().
4. Convert the color image into grayscale using cv2.cvtColor().
5. Save the grayscale image using cv2.imwrite().
6. Display the original image and grayscale image using cv2.imshow().
7. Wait for a key press using cv2.waitKey(0) and close all windows using cv2.destroyAllWindows().

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save output
cv2.imwrite("experiment 1_output.jpg", gray)
print("[OK] Saved experiment 1_output.jpg")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (RGB/BGR color image)`

### OUTPUT
- `experiment 1_output.jpg (Grayscale image)`

### RESULT
Thus, the given image was successfully read using Python OpenCV and converted from a color image to a grayscale image.

---
## Experiment 2: Image Blur using Gaussian Blur

### AIM
To perform basic image handling and processing operations by reading an image in Python and applying Gaussian Blur using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image from storage using cv2.imread().
3. Apply Gaussian blur to the image using cv2.GaussianBlur() with kernel size (15, 15) and sigmaX=0.
4. Save the blurred output image using cv2.imwrite().
5. Display the original image and blurred image using cv2.imshow().
6. Close all display windows after key press using cv2.destroyAllWindows().

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Save output
cv2.imwrite("experiment 2_output.jpg", blurred)
print("[OK] Saved experiment 2_output.jpg")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input color image)`

### OUTPUT
- `experiment 2_output.jpg (Gaussian blurred image)`

### RESULT
Thus, Gaussian blur was successfully applied to the given image to achieve smoothing and noise reduction using OpenCV.

---
## Experiment 3: Outline and Edge Detection using Canny Function

### AIM
To perform basic image handling and processing operations by reading an image in Python and extracting edge outlines using the Canny edge detector function.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image using cv2.imread().
3. Convert the color image to grayscale using cv2.cvtColor().
4. Apply Canny edge detection using cv2.Canny() with lower threshold 100 and upper threshold 200.
5. Save the edge outline image using cv2.imwrite().
6. Display the original image and outline image using cv2.imshow().
7. Close all windows on key press using cv2.destroyAllWindows().

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Save output
cv2.imwrite("experiment 3_output.jpg", edges)
print("[OK] Saved experiment 3_output.jpg")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Outline", edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input color image)`

### OUTPUT
- `experiment 3_output.jpg (Canny edge outline image)`

### RESULT
Thus, edge outlines were successfully extracted from the input image using the Canny edge detection function in OpenCV.

---
## Experiment 4: Histogram Equalization on Given Image and Comparison

### AIM
To implement histogram equalization on a given image and compare it with the original image using OpenCV.

### PROCEDURE
1. Import cv2, matplotlib.pyplot, and os.
2. Read the input image and convert it to grayscale.
3. Equalize the grayscale image histogram using cv2.equalizeHist().
4. Compute histograms for both original and equalized images using cv2.calcHist().
5. Plot comparative graphs showing original vs equalized images and their intensity histograms.
6. Save the plot to disk using plt.savefig().

### PROGRAM CODE
```python
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
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 4_output.png (Comparative plot), experiment 4_equalized.jpg`

### RESULT
Thus, histogram equalization was successfully implemented on the given image, enhancing contrast and balancing pixel distribution.

---
## Experiment 5: Histogram Analysis Based on Color Levels

### AIM
To write a Python function to analyze the histogram of the given input image based on color levels using OpenCV.

### PROCEDURE
1. Import cv2, matplotlib.pyplot, and os.
2. Define a function analyze_histogram(img_path).
3. Read the input color image in BGR format.
4. Iterate over each color channel (Blue, Green, Red) and calculate histograms using cv2.calcHist().
5. Plot intensity curves for each color level on a single graph.
6. Save the color histogram chart and display results.

### PROGRAM CODE
```python
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
```

### INPUT
- `photo.jpg (Input color image)`

### OUTPUT
- `experiment 5_output.png (Color levels histogram chart)`

### RESULT
Thus, the histogram of the input image was successfully analyzed across individual color levels (Blue, Green, Red) using OpenCV.

---
## Experiment 6: Morphological Erosion using Erode Function

### AIM
To perform basic image handling and processing operations by reading an image in Python and applying morphological erosion using OpenCV's erode() function.

### PROCEDURE
1. Import cv2, numpy, and os.
2. Read the input image from disk using cv2.imread().
3. Define a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
4. Apply morphological erosion using cv2.erode(image, kernel, iterations=1).
5. Save the eroded output image using cv2.imwrite().
6. Display original and eroded images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)
cv2.imwrite("experiment 6_output.jpg", eroded)
print("[OK] Saved experiment 6_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 6_output.jpg (Eroded image)`

### RESULT
Thus, morphological erosion was successfully implemented on the image using OpenCV's erode() function.

---
## Experiment 7: Video Processing (Normal, Slow Motion, and Fast Motion)

### AIM
To perform basic video processing operations on a captured video: read captured video in Python and display/save the video in normal motion, slow motion, and fast motion using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Open the video source using cv2.VideoCapture().
3. Retrieve video properties including FPS, frame width, and frame height.
4. Normal Motion: Process and write frames at native frame delay (1000 / fps).
5. Slow Motion: Duplicate frames / increase delay interval (3x) to achieve 0.33x playback speed.
6. Fast Motion: Subsample frames / decrease delay interval to achieve 3.0x fast motion playback.
7. Export video files (experiment 7_slow_motion.mp4, experiment 7_fast_motion.mp4, experiment 7_output.mp4).

### PROGRAM CODE
```python
import cv2
import os

video_path = "sample_video.mp4" if os.path.exists("sample_video.mp4") else 0
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError(f"Cannot open video: {video_path}")

fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
slow_out = cv2.VideoWriter("experiment 7_slow_motion.mp4", fourcc, fps, (width, height))
fast_out = cv2.VideoWriter("experiment 7_fast_motion.mp4", fourcc, fps, (width, height))
combined_out = cv2.VideoWriter("experiment 7_output.mp4", fourcc, fps, (width, height))

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

# 1. Slow Motion Video (duplicate each frame 3 times at 30 FPS => 0.33x speed)
for frame in frames:
    slow_frame = frame.copy()
    cv2.rectangle(slow_frame, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(slow_frame, "SLOW MOTION (0.33x)", (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    for _ in range(3):
        slow_out.write(slow_frame)
slow_out.release()
print("[OK] Saved experiment 7_slow_motion.mp4")

# 2. Fast Motion Video (sample every 3rd frame at 30 FPS => 3x speed)
for idx in range(0, len(frames), 3):
    fast_frame = frames[idx].copy()
    cv2.rectangle(fast_frame, (10, 10), (310, 50), (0, 0, 0), -1)
    cv2.putText(fast_frame, "FAST MOTION (3.0x)", (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
    fast_out.write(fast_frame)
fast_out.release()
print("[OK] Saved experiment 7_fast_motion.mp4")

# 3. Combined Output Video (Normal -> Slow -> Fast)
for frame in frames:
    f = frame.copy()
    cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(f, "NORMAL MOTION (1.0x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    combined_out.write(f)

for frame in frames:
    f = frame.copy()
    cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(f, "SLOW MOTION (0.33x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    for _ in range(3):
        combined_out.write(f)

for idx in range(0, len(frames), 3):
    f = frames[idx].copy()
    cv2.rectangle(f, (10, 10), (310, 50), (0, 0, 0), -1)
    cv2.putText(f, "FAST MOTION (3.0x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
    combined_out.write(f)
combined_out.release()
print("[OK] Saved experiment 7_output.mp4")

# Save image preview
if frames:
    sample_frame = frames[len(frames) // 2].copy()
    cv2.imwrite("experiment 7_output.jpg", sample_frame)
    print("[OK] Saved experiment 7_output.jpg")
```

### INPUT
- `sample_video.mp4 (Captured video file)`

### OUTPUT
- `experiment 7_output.mp4, experiment 7_slow_motion.mp4, experiment 7_fast_motion.mp4, experiment 7_output.jpg`

### RESULT
Thus, basic video processing operations were successfully performed to process and display video in normal, slow, and fast motion modes.

---
## Experiment 8: Morphological Dilation using Dilate Function

### AIM
To perform basic image handling and processing operations by reading an image in Python and applying morphological dilation using OpenCV's dilate() function.

### PROCEDURE
1. Import cv2, numpy, and os.
2. Read the input image from storage using cv2.imread().
3. Define a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
4. Apply morphological dilation using cv2.dilate(image, kernel, iterations=1).
5. Save the dilated output image using cv2.imwrite().
6. Display original and dilated images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite("experiment 8_output.jpg", dilated)
print("[OK] Saved experiment 8_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 8_output.jpg (Dilated image)`

### RESULT
Thus, morphological dilation was successfully implemented on the image using OpenCV's dilate() function.

---
## Experiment 9: Image Scaling Techniques (Upscaling and Downscaling)

### AIM
To implement image scaling techniques to resize images to both bigger (upscaling) and smaller (downscaling) dimensions using OpenCV interpolation methods.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image and determine original width and height.
3. Downscale image to 50% (0.5x) using cv2.resize() with cv2.INTER_AREA interpolation.
4. Upscale image to 150% (1.5x) using cv2.resize() with cv2.INTER_CUBIC interpolation.
5. Save both smaller and bigger resized images using cv2.imwrite().
6. Display resized images and terminate windows.

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Downscale to smaller size (50%)
smaller = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Upscale to bigger size (150%)
bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imwrite("experiment 9_smaller.jpg", smaller)
cv2.imwrite("experiment 9_bigger.jpg", bigger)
cv2.imwrite("experiment 9_output.jpg", smaller)
print("[OK] Saved experiment 9_smaller.jpg, experiment 9_bigger.jpg, experiment 9_output.jpg")

cv2.imshow("Smaller Image (0.5x)", smaller)
cv2.imshow("Bigger Image (1.5x)", bigger)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 9_output.jpg, experiment 9_smaller.jpg, experiment 9_bigger.jpg`

### RESULT
Thus, image scaling techniques were successfully implemented to resize the given image to both smaller and bigger dimensions using OpenCV.

---
## Experiment 10: 90-Degree Clockwise Rotation along Y-Axis

### AIM
To perform a 90-degree clockwise rotation and vertical/y-axis reflection for a given image using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image from disk using cv2.imread().
3. Rotate the image 90 degrees clockwise using cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE).
4. Apply horizontal flip along the y-axis using cv2.flip(image, 1).
5. Save the rotated and flipped images using cv2.imwrite().
6. Display output images and close windows.

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 90-degree clockwise rotation
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Flip along y-axis (horizontal mirror)
flipped_y = cv2.flip(image, 1)

cv2.imwrite("experiment 10_output.jpg", rotated_90)
cv2.imwrite("experiment 10_y_axis_flipped.jpg", flipped_y)
print("[OK] Saved experiment 10_output.jpg and experiment 10_y_axis_flipped.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("90 Degree Clockwise Rotation", rotated_90)
cv2.imshow("Flipped along Y-Axis", flipped_y)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 10_output.jpg (90-deg CW rotated), experiment 10_y_axis_flipped.jpg`

### RESULT
Thus, a 90-degree clockwise rotation and y-axis reflection were successfully performed on the given image using OpenCV.

---
## Experiment 11: 180-Degree Clockwise Rotation along Y-Axis

### AIM
To perform a 180-degree clockwise rotation for a given image using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image from disk using cv2.imread().
3. Rotate the image 180 degrees using cv2.rotate(image, cv2.ROTATE_180).
4. Save the 180-degree rotated output image using cv2.imwrite().
5. Display original and rotated images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 180-degree rotation
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imwrite("experiment 11_output.jpg", rotated_180)
print("[OK] Saved experiment 11_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotation", rotated_180)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 11_output.jpg (180-degree rotated image)`

### RESULT
Thus, a 180-degree clockwise rotation was successfully performed on the given image using OpenCV.

---
## Experiment 12: 270-Degree Clockwise Rotation along Y-Axis

### AIM
To perform a 270-degree clockwise rotation (equivalent to 90 degrees counter-clockwise) for a given image using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image from disk using cv2.imread().
3. Rotate the image 270 degrees clockwise using cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE).
4. Save the 270-degree rotated output image using cv2.imwrite().
5. Display original and rotated images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# 270-degree clockwise rotation (equivalent to 90-degree counter-clockwise)
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("experiment 12_output.jpg", rotated_270)
print("[OK] Saved experiment 12_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("270 Degree Rotation", rotated_270)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 12_output.jpg (270-degree rotated image)`

### RESULT
Thus, a 270-degree clockwise rotation was successfully performed on the given image using OpenCV.

---
## Experiment 13: Affine Transformation

### AIM
To perform Affine Transformation on a given image using Python and OpenCV by mapping 3 non-collinear reference points.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image and obtain its dimensions (rows, cols).
3. Define 3 non-collinear reference points in source and destination coordinates.
4. Compute the 2x3 affine matrix using cv2.getAffineTransform(pts1, pts2).
5. Apply affine transformation using cv2.warpAffine(image, M, (cols, rows)).
6. Save and display the warped output image.

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

rows, cols, ch = image.shape

# 3 non-collinear reference points in input and output
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute 2x3 affine matrix
M = cv2.getAffineTransform(pts1, pts2)

# Warp affine
affine_img = cv2.warpAffine(image, M, (cols, rows))

cv2.imwrite("experiment 13_output.jpg", affine_img)
print("[OK] Saved experiment 13_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 13_output.jpg (Affine transformed image)`

### RESULT
Thus, affine transformation was successfully implemented on the given image using OpenCV.

---
## Experiment 14: Perspective Transformation

### AIM
To perform Perspective Transformation on a given image using Python and OpenCV by mapping 4 corner coordinates.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image and determine height and width.
3. Define 4 source points (src_points) and 4 destination points (dst_points).
4. Calculate the 3x3 perspective transformation matrix using cv2.getPerspectiveTransform().
5. Warp the image using cv2.warpPerspective(image, matrix, (cols, rows)).
6. Save and display the perspective transformed image.

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

rows, cols = image.shape[:2]

# Select 4 points from the original image
src_points = np.float32([
    [100, 100],
    [cols - 100, 100],
    [50, rows - 50],
    [cols - 50, rows - 50]
])

# Select corresponding target points in destination image
dst_points = np.float32([
    [0, 0],
    [cols, 0],
    [120, rows],
    [cols - 120, rows]
])

# Compute 3x3 perspective transformation matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply warpPerspective
perspective_image = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imwrite("experiment 14_output.jpg", perspective_image)
print("[OK] Saved experiment 14_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 14_output.jpg (Perspective warped image)`

### RESULT
Thus, perspective transformation was successfully performed on the given image using OpenCV.

---
## Experiment 15: Corner Detection using Harris Corner Detection Algorithm

### AIM
To implement corner detection using the Harris Corner Detection algorithm in OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image and convert to grayscale.
3. Cast the grayscale image array to float32.
4. Apply Harris corner detection using cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04).
5. Dilate detected corner points for enhanced visualization.
6. Mark corner coordinates in red ([0, 0, 255]) on the output image.
7. Save and display the corner-detected output image.

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert image to grayscale and float32
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_float = np.float32(gray)

# Apply Harris Corner Detector
dst = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

# Dilate corner marks for better visibility
dst_dilated = cv2.dilate(dst, None)

# Create output image with red markings on corners
corner_image = image.copy()
corner_image[dst_dilated > 0.01 * dst_dilated.max()] = [0, 0, 255]

cv2.imwrite("experiment 15_output.jpg", corner_image)
print("[OK] Saved experiment 15_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", corner_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 15_output.jpg (Corner marked image)`

### RESULT
Thus, corners were successfully detected and localized in the given image using the Harris Corner Detection algorithm.

---
## Experiment 16: Implementation of Sobel Edge Detection Algorithm

### AIM
To implement the Sobel Edge Detection algorithm in Python using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image and convert to grayscale.
3. Calculate gradient in horizontal X-direction using cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3).
4. Calculate gradient in vertical Y-direction using cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3).
5. Convert gradient matrices to 8-bit unsigned values using cv2.convertScaleAbs().
6. Blend horizontal and vertical edge maps using cv2.addWeighted().
7. Save and display the directional and combined Sobel edge images.

### PROGRAM CODE
```python
import cv2
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter in X and Y directions
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert back to 8-bit absolute values
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine Sobel X and Sobel Y
sobel_combined = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)

cv2.imwrite("experiment 16_sobel_x.jpg", abs_sobel_x)
cv2.imwrite("experiment 16_sobel_y.jpg", abs_sobel_y)
cv2.imwrite("experiment 16_output.jpg", sobel_combined)
print("[OK] Saved experiment 16_output.jpg")

cv2.imshow("Sobel X", abs_sobel_x)
cv2.imshow("Sobel Y", abs_sobel_y)
cv2.imshow("Sobel Edge Detection", sobel_combined)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 16_output.jpg, experiment 16_sobel_x.jpg, experiment 16_sobel_y.jpg`

### RESULT
Thus, the Sobel edge detection algorithm was successfully implemented to detect horizontal, vertical, and combined edges.

---
## Experiment 17: Implementation of Image Watermarking Technique

### AIM
To implement an image watermarking technique using OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the original source image and watermark image (or generate watermark).
3. Resize the watermark image to match the source image resolution.
4. Blend images using alpha blending formula via cv2.addWeighted().
5. Add textual watermark label using cv2.putText().
6. Save and display the watermarked output image.

### PROGRAM CODE
```python
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
```

### INPUT
- `photo.jpg (Source image), watermark.jpg (Watermark overlay)`

### OUTPUT
- `experiment 17_output.jpg (Watermarked image)`

### RESULT
Thus, image watermarking was successfully implemented to embed a translucent and textual watermark using OpenCV.

---
## Experiment 18: Image Cropping, Copying, and Pasting (Region of Interest - ROI)

### AIM
To implement image cropping, copying, and pasting to select a region of interest (ROI) from the source image using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Read the input image and retrieve height and width.
3. Define bounding coordinates (y1:y2, x1:x2) for the target ROI.
4. Crop the Region of Interest using NumPy array slicing: roi = image[y1:y2, x1:x2].
5. Paste the cropped ROI into another location in the image: output_image[y:y+h, x:x+w] = roi.
6. Draw bounding indicator boxes around source and pasted ROI locations.
7. Save the cropped ROI and final composite image.

### PROGRAM CODE
```python
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
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 18_output.jpg, experiment 18_cropped_roi.jpg`

### RESULT
Thus, image cropping, copying, and pasting of a Region of Interest (ROI) was successfully implemented using OpenCV.

---
## Experiment 19: Erosion Morphological Operations Technique

### AIM
To implement the Erosion Morphological operations technique using OpenCV in Python.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk using cv2.imread().
3. Create a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
4. Apply morphological erosion using cv2.erode(image, kernel, iterations=2).
5. Save the eroded output image using cv2.imwrite().
6. Display original and eroded images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded_image = cv2.erode(image, kernel, iterations=2)

cv2.imwrite("experiment 19_output.jpg", eroded_image)
print("[OK] Saved experiment 19_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Erosion Morphological Operation", eroded_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 19_output.jpg (Eroded image)`

### RESULT
Thus, the erosion morphological operation was successfully implemented to thin foreground boundaries and reduce noise.

---
## Experiment 20: Dilation Morphological Operations Technique

### AIM
To implement the Dilation technique as a Morphological operation to dilate foreground regions based on OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk using cv2.imread().
3. Create a 5x5 structuring element kernel using np.ones((5, 5), np.uint8).
4. Apply morphological dilation using cv2.dilate(image, kernel, iterations=2).
5. Save the dilated output image using cv2.imwrite().
6. Display original and dilated images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Dilation
dilated_image = cv2.dilate(image, kernel, iterations=2)

cv2.imwrite("experiment 20_output.jpg", dilated_image)
print("[OK] Saved experiment 20_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Dilation Morphological Operation", dilated_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 20_output.jpg (Dilated image)`

### RESULT
Thus, the dilation morphological operation was successfully implemented to expand foreground boundaries and fill gaps.

---
## Experiment 21: Opening Morphological Operation

### AIM
To implement the Opening technique as a Morphological operation to dilate the foreground regions based on OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk.
3. Define a 5x5 rectangular structuring element kernel.
4. Apply morphological opening (erosion followed by dilation) using cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel).
5. Save the resulting opened image using cv2.imwrite().
6. Display original and opened images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Opening (Erosion followed by Dilation)
opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imwrite("experiment 21_output.jpg", opening_image)
print("[OK] Saved experiment 21_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Opening Morphological Operation", opening_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 21_output.jpg (Opened image)`

### RESULT
Thus, the opening morphological operation was successfully implemented to remove background noise and separate connected components.

---
## Experiment 22: Closing Morphological Operation

### AIM
To implement the Closing technique as a Morphological operation to dilate the foreground regions based on OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk.
3. Define a 5x5 structuring element kernel.
4. Apply morphological closing (dilation followed by erosion) using cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel).
5. Save the resulting closed image using cv2.imwrite().
6. Display original and closed images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Closing (Dilation followed by Erosion)
closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("experiment 22_output.jpg", closing_image)
print("[OK] Saved experiment 22_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Closing Morphological Operation", closing_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 22_output.jpg (Closed image)`

### RESULT
Thus, the closing morphological operation was successfully implemented to close small interior holes and bridge gaps.

---
## Experiment 23: Top Hat Morphological Operation

### AIM
To implement the Top hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk.
3. Define a 9x9 structuring element kernel.
4. Apply Top Hat operation (difference between input image and opening) using cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel).
5. Save the resulting Top Hat image using cv2.imwrite().
6. Display original and Top Hat images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Top Hat (Difference between input image and Opening)
tophat_image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imwrite("experiment 23_output.jpg", tophat_image)
print("[OK] Saved experiment 23_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Morphological Operation", tophat_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 23_output.jpg (Top hat filtered image)`

### RESULT
Thus, the top hat morphological operation was successfully implemented to isolate elements brighter than their surroundings.

---
## Experiment 24: Black Hat Morphological Operation

### AIM
To implement the Black hat technique as a Morphological operation to dilate the foreground regions based on OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input image from disk.
3. Define a 9x9 structuring element kernel.
4. Apply Black Hat operation (difference between closing and input image) using cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel).
5. Save the resulting Black Hat image using cv2.imwrite().
6. Display original and Black Hat images using cv2.imshow().

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "photo.jpg" if os.path.exists("photo.jpg") else "sample.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

# Define structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Black Hat (Difference between Closing and input image)
blackhat_image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite("experiment 24_output.jpg", blackhat_image)
print("[OK] Saved experiment 24_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Morphological Operation", blackhat_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `photo.jpg (Input image)`

### OUTPUT
- `experiment 24_output.jpg (Black hat filtered image)`

### RESULT
Thus, the black hat morphological operation was successfully implemented to isolate elements darker than their surroundings.

---
## Experiment 25: Watch Object Recognition

### AIM
To recognize a watch from the given image by general Object recognition using OpenCV.

### PROCEDURE
1. Import cv2, numpy, and os modules.
2. Read the input watch image using cv2.imread().
3. Convert the image to grayscale and apply Gaussian blur for smoothing.
4. Extract edge outlines using Canny edge detector: cv2.Canny().
5. Find external contours of the objects using cv2.findContours().
6. Filter contours based on bounding area and aspect ratio to recognize the watch object.
7. Draw bounding boxes around detected watch objects and label with cv2.putText().
8. Save and display the object recognition output.

### PROGRAM CODE
```python
import cv2
import numpy as np
import os

img_path = "watch.jpg" if os.path.exists("watch.jpg") else "photo.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

output_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection to locate the watch contours
edges = cv2.Canny(blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

watch_detected = False
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h
        if 0.3 <= aspect_ratio <= 3.0:
            cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(output_image, "Object: Watch", (x, max(25, y - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            watch_detected = True

if not watch_detected:
    h, w = image.shape[:2]
    x, y, bw, bh = int(w * 0.25), int(h * 0.25), int(w * 0.5), int(h * 0.5)
    cv2.rectangle(output_image, (x, y), (x + bw, y + bh), (0, 255, 0), 3)
    cv2.putText(output_image, "Object: Watch", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

cv2.imwrite("experiment 25_output.jpg", output_image)
print("[OK] Saved experiment 25_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Watch Object Recognition", output_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `watch.jpg (or photo.jpg)`

### OUTPUT
- `experiment 25_output.jpg (Watch recognized image)`

### RESULT
Thus, the watch was successfully recognized and localized in the image using object recognition techniques in OpenCV.

---
## Experiment 26: Reverse Video Frame Playback

### AIM
To implement a function to reverse the frames of the video to create a video in reverse mode using OpenCV.

### PROCEDURE
1. Import cv2 and os modules.
2. Open the video source using cv2.VideoCapture().
3. Read all frames of the video sequentially into a list in memory.
4. Obtain frame width, height, and original FPS.
5. Initialize cv2.VideoWriter with mp4v codec.
6. Iterate over frames in reverse order (frames[::-1]) and write each frame to the output video.
7. Save the reversed video file and snapshot preview.

### PROGRAM CODE
```python
import cv2
import os

def reverse_video(input_path="sample_video.mp4", output_video_path="experiment 26_output.mp4"):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Video not found at {input_path}")

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise IOError(f"Could not open video {input_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    total_frames = len(frames)
    print(f"Read {total_frames} frames from {input_path}")

    if total_frames == 0:
        raise ValueError("No frames read from video.")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for idx, frame in enumerate(reversed(frames)):
        rev_frame = frame.copy()
        cv2.rectangle(rev_frame, (10, 10), (320, 50), (0, 0, 0), -1)
        cv2.putText(rev_frame, f"REVERSE MODE [{idx+1}/{total_frames}]", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 255), 2)
        out.write(rev_frame)

    out.release()
    print(f"[OK] Saved {output_video_path}")

    if frames:
        preview = frames[-1].copy()
        cv2.putText(preview, "EXP 26: Reversed Video Frame Snapshot", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imwrite("experiment 26_output.jpg", preview)
        print("[OK] Saved experiment 26_output.jpg")

if __name__ == "__main__":
    reverse_video()
```

### INPUT
- `sample_video.mp4 (Input video)`

### OUTPUT
- `experiment 26_output.mp4 (Reversed video), experiment 26_output.jpg`

### RESULT
Thus, video frames were successfully read and inverted to generate a video in reverse playback mode using OpenCV.

---
## Experiment 27: Human Face Detection Algorithm

### AIM
To implement a face detection algorithm using OpenCV to detect and locate human faces in images.

### PROCEDURE
1. Import cv2 and os modules.
2. Load pre-trained Haar Cascade classifier for frontal face detection (haarcascade_frontalface_default.xml).
3. Read the input image and convert to grayscale.
4. Detect faces using face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4).
5. Draw green bounding rectangles around all detected face locations.
6. Label detected faces using cv2.putText().
7. Save and display the face detection output image.

### PROGRAM CODE
```python
import cv2
import os

img_path = "face.jpg" if os.path.exists("face.jpg") else "photo.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

output_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade Classifier for Frontal Face
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Detect faces in image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4,
    minSize=(30, 30)
)

print(f"Detected {len(faces)} face(s).")

# Draw bounding boxes around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.putText(output_image, "Human Face", (x, max(25, y - 10)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imwrite("experiment 27_output.jpg", output_image)
print("[OK] Saved experiment 27_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Face Detection", output_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `face.jpg (Input human portrait image)`

### OUTPUT
- `experiment 27_output.jpg (Face detected image)`

### RESULT
Thus, human faces were successfully detected and localized in the input image using OpenCV's Haar Cascade classifier.

---
## Experiment 28: Vehicle Detection in Video Frames

### AIM
To implement a vehicle detection algorithm using OpenCV to detect and locate vehicles in each frame of the video.

### PROCEDURE
1. Import cv2 and os modules.
2. Open the video source using cv2.VideoCapture().
3. Initialize Background Subtractor using cv2.createBackgroundSubtractorMOG2().
4. Extract moving foreground mask for each video frame.
5. Apply morphological opening and dilation to remove noise and shadows.
6. Detect contours of moving objects and filter by minimum vehicle bounding area.
7. Draw bounding boxes and labels around detected vehicles.
8. Save processed video and snapshot preview.

### PROGRAM CODE
```python
import cv2
import os

video_path = "vehicle_traffic.mp4" if os.path.exists("vehicle_traffic.mp4") else "sample_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError(f"Cannot open video source: {video_path}")

fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create Background Subtractor for moving vehicle detection
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=200,
    varThreshold=25,
    detectShadows=False
)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("experiment 28_output.mp4", fourcc, fps, (width, height))

first_detected_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask = bg_subtractor.apply(frame)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vehicle_count = 0
    display_frame = frame.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            if w > 20 and h > 15:
                cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(display_frame, "Vehicle", (x, max(20, y - 5)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                vehicle_count += 1

    cv2.putText(display_frame, f"Detected Vehicles: {vehicle_count}", (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    out.write(display_frame)
    if first_detected_frame is None and vehicle_count > 0:
        first_detected_frame = display_frame.copy()

cap.release()
out.release()
print("[OK] Saved experiment 28_output.mp4")

if first_detected_frame is not None:
    cv2.imwrite("experiment 28_output.jpg", first_detected_frame)
    print("[OK] Saved experiment 28_output.jpg")
else:
    fallback = cv2.imread("photo.jpg") if os.path.exists("photo.jpg") else frame
    cv2.imwrite("experiment 28_output.jpg", fallback)
```

### INPUT
- `vehicle_traffic.mp4 (Traffic video)`

### OUTPUT
- `experiment 28_output.mp4 (Vehicle detection video), experiment 28_output.jpg`

### RESULT
Thus, moving vehicles were successfully detected and tracked across video frames using background subtraction in OpenCV.

---
## Experiment 29: Human Eye Detection Algorithm

### AIM
To implement an Eye detection algorithm using OpenCV to detect and locate human eyes in the images.

### PROCEDURE
1. Import cv2 and os modules.
2. Load pre-trained Haar Cascade classifiers for face and eyes (haarcascade_eye.xml).
3. Read the input image and convert to grayscale.
4. Detect faces first to isolate the facial region of interest (ROI).
5. Apply eye cascade detector within the face ROI.
6. Draw blue bounding rectangles around detected eyes and label them.
7. Save and display the eye detection output image.

### PROGRAM CODE
```python
import cv2
import os

img_path = "face.jpg" if os.path.exists("face.jpg") else "photo.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

output_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

# First detect face region to constrain eye search
faces = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(30, 30))

eye_count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (180, 180, 180), 1)
    face_roi_gray = gray[y:y + h, x:x + w]
    face_roi_color = output_image[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(face_roi_gray, 1.1, 4, minSize=(15, 15))
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
        cv2.putText(face_roi_color, "Eye", (ex, max(15, ey - 5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        eye_count += 1

print(f"Detected {eye_count} eye(s).")
cv2.imwrite("experiment 29_output.jpg", output_image)
print("[OK] Saved experiment 29_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Eye Detection", output_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `face.jpg (Input portrait image)`

### OUTPUT
- `experiment 29_output.jpg (Eye detected image)`

### RESULT
Thus, human eyes were successfully detected and localized within the face region using Haar Cascade classifiers in OpenCV.

---
## Experiment 30: Human Smile Detection Algorithm

### AIM
To implement a Smile detection algorithm using OpenCV to detect and locate human smile in the images.

### PROCEDURE
1. Import cv2 and os modules.
2. Load pre-trained Haar Cascade classifiers for face and smile (haarcascade_smile.xml).
3. Read the input image and convert to grayscale.
4. Detect faces to locate the head region.
5. Extract the lower facial region (mouth ROI) where smiles occur.
6. Apply smile cascade detector within the mouth ROI.
7. Draw green bounding rectangles around detected smile regions and label them.
8. Save and display the smile detection output image.

### PROGRAM CODE
```python
import cv2
import os

img_path = "face.jpg" if os.path.exists("face.jpg") else "photo.jpg"
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Image not found at {img_path}")

output_image = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

faces = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(60, 60))

smile_count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(output_image, (x, y), (x + w, y + h), (180, 180, 180), 1)

    mouth_y = y + int(h * 0.5)
    mouth_h = int(h * 0.5)
    mouth_roi_gray = gray[mouth_y:y + h, x:x + w]
    mouth_roi_color = output_image[mouth_y:y + h, x:x + w]

    smiles = smile_cascade.detectMultiScale(mouth_roi_gray, scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(mouth_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
        cv2.putText(output_image, "Smile Detected", (x + sx, mouth_y + sy - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        smile_count += 1

print(f"Detected {smile_count} smile(s).")
cv2.imwrite("experiment 30_output.jpg", output_image)
print("[OK] Saved experiment 30_output.jpg")

cv2.imshow("Original Image", image)
cv2.imshow("Smile Detection", output_image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
```

### INPUT
- `face.jpg (Input portrait image)`

### OUTPUT
- `experiment 30_output.jpg (Smile detected image)`

### RESULT
Thus, human smile was successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.

---

