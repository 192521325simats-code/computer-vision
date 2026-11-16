"""
EXPERIMENT 30: Implement a Smile detection algorithm using OpenCV to detect and locate human smile in the images.

AIM:
    To detect and locate human smiles in an image using the Haar Feature-based Smile Cascade Classifier in OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Load face and smile Haar Cascade classifiers (haarcascade_smile.xml).
    3. Read input portrait image and convert to grayscale.
    4. Detect faces to localize the facial region.
    5. Extract the lower mouth ROI within the detected face boundary.
    6. Apply the smile detector using smile_cascade.detectMultiScale().
    7. Draw green bounding boxes around detected smiles.
    8. Save and display the final smile-detected output image.

INPUT:
    face.jpg (Source image)

OUTPUT:
    experiment 30_output.jpg (Output image)

RESULT:
    Thus, human smiles were successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("face.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

output = image.copy()
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    mouth_roi_gray = gray[y + int(h * 0.5):y + h, x:x + w]
    mouth_roi_color = output[y + int(h * 0.5):y + h, x:x + w]
    smiles = smile_cascade.detectMultiScale(mouth_roi_gray, 1.2, 5)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(mouth_roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
        cv2.putText(mouth_roi_color, "Smile", (sx, sy - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

cv2.imwrite("experiment 30_output.jpg", output)
print("Smile detection complete.")

print("RESULT: Thus, human smiles were successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.")
