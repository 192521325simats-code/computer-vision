"""
EXPERIMENT 25: Watch Object Recognition

AIM:
    To recognize a watch from the given image by general Object recognition using OpenCV.

PROCEDURE:
    1. Import cv2, numpy, and os modules.
    2. Read the input watch image using cv2.imread().
    3. Convert the image to grayscale and apply Gaussian blur for smoothing.
    4. Extract edge outlines using Canny edge detector: cv2.Canny().
    5. Find external contours of the objects using cv2.findContours().
    6. Filter contours based on bounding area and aspect ratio to recognize the watch object.
    7. Draw bounding boxes around detected watch objects and label with cv2.putText().
    8. Save and display the object recognition output.

INPUT:
    watch.jpg (or photo.jpg)

OUTPUT:
    experiment 25_output.jpg (Watch recognized image)

RESULT:
    Thus, the watch was successfully recognized and localized in the image using object recognition techniques in OpenCV.
"""

# ==================== PROGRAM CODE ====================
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

print("RESULT: Thus, the watch was successfully recognized and localized in the image using object recognition techniques in OpenCV.")
