"""
EXPERIMENT 27: Implement a face detection algorithm using OpenCV to detect and locate human faces in the images.

AIM:
    To detect and locate human faces in an image using the pre-trained Haar Feature-based Cascade Classifier in OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Load the Haar Cascade classifier for frontal faces (haarcascade_frontalface_default.xml).
    3. Read the input portrait image (face.jpg) and convert it to grayscale.
    4. Detect faces using face_cascade.detectMultiScale() with scaleFactor=1.1 and minNeighbors=5.
    5. Iterate through detected coordinates (x, y, w, h) and draw bounding rectangles.
    6. Label detected faces as 'Face'.
    7. Save and display the annotated face detection image.

INPUT:
    face.jpg (Source image)

OUTPUT:
    experiment 27_output.jpg (Output image)

RESULT:
    Thus, human faces were successfully detected and localized with bounding boxes using Haar Cascade classifiers in OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("face.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

output = image.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(output, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imwrite("experiment 27_output.jpg", output)
print("Face detection complete.")

print("RESULT: Thus, human faces were successfully detected and localized with bounding boxes using Haar Cascade classifiers in OpenCV.")
