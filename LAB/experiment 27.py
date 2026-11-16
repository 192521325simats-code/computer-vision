"""
EXPERIMENT 27
Aim: Implement a face detection algorithm using OpenCV to detect and locate human faces in images.
"""
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
