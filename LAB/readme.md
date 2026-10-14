# Computer Vision Laboratory Experiments

This folder contains the complete list of 13 Computer Vision and Digital Image Processing experiments using Python and OpenCV. Each experiment has its own separate program code file and corresponding output image file.

---

## Index of Experiments

| No. | Experiment Name | Program File | Output File |
|:---:|:----------------|:-------------|:------------|
| 1 | Read Image and Convert to Grayscale | `experiment 1.py` | `experiment 1_output.jpg` |
| 2 | Image Blur using Gaussian Blur | `experiment 2.py` | `experiment 2_output.jpg` |
| 3 | Outline / Edge Detection using Canny | `experiment 3.py` | `experiment 3_output.jpg` |
| 4 | Histogram Equalization & Comparison | `experiment 4.py` | `experiment 4_output.png` |
| 5 | Color Histogram Analysis by Color Levels | `experiment 5.py` | `experiment 5_output.png` |
| 6 | Morphological Erosion using Erode Function | `experiment 6.py` | `experiment 6_output.jpg` |
| 7 | Video Processing (Normal, Slow, and Fast Motion) | `experiment 7.py` | `experiment 7_output.jpg` |
| 8 | Morphological Dilation using Dilate Function | `experiment 8.py` | `experiment 8_output.jpg` |
| 9 | Image Scaling (Upscaling and Downscaling) | `experiment 9.py` | `experiment 9_output.jpg` |
| 10 | 90-Degree Clockwise Rotation | `experiment 10.py` | `experiment 10_output.jpg` |
| 11 | 180-Degree Clockwise Rotation | `experiment 11.py` | `experiment 11_output.jpg` |
| 12 | 270-Degree Clockwise Rotation | `experiment 12.py` | `experiment 12_output.jpg` |
| 13 | Affine Transformation | `experiment 13.py` | `experiment 13_output.jpg` |

---

## Experiment Details

### 1. Convert an Image to Gray-scale
- **Program File**: `experiment 1.py`
- **Output File**: `experiment 1_output.jpg`
```python
import cv2
image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("experiment 1_output.jpg", gray)
```

### 2. Convert an Image to Blur using Gaussian Blur
- **Program File**: `experiment 2.py`
- **Output File**: `experiment 2_output.jpg`
```python
import cv2
image = cv2.imread("photo.jpg")
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite("experiment 2_output.jpg", blurred)
```

### 3. Convert an Image to show outline using Canny function
- **Program File**: `experiment 3.py`
- **Output File**: `experiment 3_output.jpg`
```python
import cv2
image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
cv2.imwrite("experiment 3_output.jpg", edges)
```

### 4. Implement histogram equalization on the given image and compare it with the original image
- **Program File**: `experiment 4.py`
- **Output File**: `experiment 4_output.png`
```python
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
```

### 5. Write a Python function to analyze the histogram of the given input image based on color levels
- **Program File**: `experiment 5.py`
- **Output File**: `experiment 5_output.png`
```python
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(img_path):
    image = cv2.imread(img_path)
    for i, col in enumerate(('b', 'g', 'r')):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
```

### 6. Convert an Image to erode using Erode function
- **Program File**: `experiment 6.py`
- **Output File**: `experiment 6_output.jpg`
```python
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(image, kernel, iterations=1)
cv2.imwrite("experiment 6_output.jpg", eroded)
```

### 7. Video processing: display captured video in slow motion and in fast motion
- **Program File**: `experiment 7.py`
- **Output File**: `experiment 7_output.jpg`
```python
import cv2

cap = cv2.VideoCapture("sample_video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
normal_delay = int(1000 / fps)
slow_delay = int(normal_delay * 3)       # Slow motion
fast_delay = max(1, int(normal_delay / 3)) # Fast motion
```

### 8. Dilate an Image using Dilate function
- **Program File**: `experiment 8.py`
- **Output File**: `experiment 8_output.jpg`
```python
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(image, kernel, iterations=1)
cv2.imwrite("experiment 8_output.jpg", dilated)
```

### 9. Image scaling techniques to resize the images to both bigger and small sizes
- **Program File**: `experiment 9.py`
- **Output File**: `experiment 9_output.jpg`
```python
import cv2

image = cv2.imread("photo.jpg")
smaller = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
bigger = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
```

### 10. Perform a 90-degree rotation clockwise along the y-axis for the given image
- **Program File**: `experiment 10.py`
- **Output File**: `experiment 10_output.jpg`
```python
import cv2

image = cv2.imread("photo.jpg")
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
flipped_y = cv2.flip(image, 1)
```

### 11. Perform a 180-degree rotation clockwise along the y-axis for the given image
- **Program File**: `experiment 11.py`
- **Output File**: `experiment 11_output.jpg`
```python
import cv2

image = cv2.imread("photo.jpg")
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)
```

### 12. Perform a 270-degree rotation clockwise along the y-axis for the given image
- **Program File**: `experiment 12.py`
- **Output File**: `experiment 12_output.jpg`
```python
import cv2

image = cv2.imread("photo.jpg")
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
```

### 13. Perform Affine Transformation on the given image using Python and OpenCV
- **Program File**: `experiment 13.py`
- **Output File**: `experiment 13_output.jpg`
```python
import cv2
import numpy as np

image = cv2.imread("photo.jpg")
rows, cols, ch = image.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
affine_img = cv2.warpAffine(image, M, (cols, rows))
```
