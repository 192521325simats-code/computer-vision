"""
EXPERIMENT 29: Implement an Eye detection algorithm using OpenCV to detect and locate human eyes in the images.

AIM:
    To detect and locate human eyes in an image using the Haar Feature-based Eye Cascade Classifier in OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Load Haar Cascade classifiers for both face and eye detection (haarcascade_eye.xml).
    3. Read input portrait image and convert to grayscale.
    4. Detect facial boundaries to define regions of interest (ROI) for eyes.
    5. Detect eyes within the upper facial ROI using eye_cascade.detectMultiScale().
    6. Draw blue/green bounding rectangles or circles around detected eyes.
    7. Save and display the annotated eye detection image.

INPUT:
    face.jpg (Source image)

OUTPUT:
    experiment 29_output.jpg (Output image)

RESULT:
    Thus, human eyes were successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("face.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

output = image.copy()
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = output[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
        cv2.putText(roi_color, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imwrite("experiment 29_output.jpg", output)
print("Eye detection complete.")

print("RESULT: Thus, human eyes were successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.")
