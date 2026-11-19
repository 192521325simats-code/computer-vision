"""
EXPERIMENT 38: Write a Python function to Count the number of faces for the given input image using Open CV.

AIM:
    To detect, locate, and count the total number of human faces present in a given input image using Haar Cascade Classifiers in OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Load the pre-trained Haar Cascade frontal face classifier (haarcascade_frontalface_default.xml).
    3. Read the input group portrait image and convert it to grayscale.
    4. Detect all faces in the image using face_cascade.detectMultiScale().
    5. Count the total number of detected bounding boxes (len(faces)).
    6. Loop through each detected face, draw green bounding boxes, and label each with its face index.
    7. Display a top banner stating 'TOTAL FACES DETECTED: {count}'.
    8. Save and display the annotated output image.

INPUT:
    faces_group.jpg (Source image)

OUTPUT:
    experiment 38_output.jpg (Output image)

RESULT:
    Thus, the number of human faces in the given input image was successfully detected and counted using OpenCV Haar Cascades.
"""

# ==================== PROGRAM CODE ====================
import cv2

image = cv2.imread("faces_group.jpg")
if image is None:
    image = cv2.imread("face.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(50, 50))

output = image.copy()
total_faces = len(faces)

for idx, (x, y, w, h) in enumerate(faces, 1):
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(output, f"Face #{idx}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Top header banner showing total count
cv2.rectangle(output, (0, 0), (output.shape[1], 45), (40, 40, 40), -1)
cv2.putText(output, f"TOTAL FACES DETECTED: {total_faces}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

# Save and display
cv2.imwrite("experiment 38_output.jpg", output)
cv2.imshow("Face Counter Output", output)
cv2.waitKey(1000)
cv2.destroyAllWindows()
print(f"Total faces counted: {total_faces}")

print("RESULT: Thus, the number of human faces in the given input image was successfully detected and counted using OpenCV Haar Cascades.")
