"""
EXPERIMENT 29: Human Eye Detection Algorithm

AIM:
    To implement an Eye detection algorithm using OpenCV to detect and locate human eyes in the images.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Load pre-trained Haar Cascade classifiers for face and eyes (haarcascade_eye.xml).
    3. Read the input image and convert to grayscale.
    4. Detect faces first to isolate the facial region of interest (ROI).
    5. Apply eye cascade detector within the face ROI.
    6. Draw blue bounding rectangles around detected eyes and label them.
    7. Save and display the eye detection output image.

INPUT:
    face.jpg (Input portrait image)

OUTPUT:
    experiment 29_output.jpg (Eye detected image)

RESULT:
    Thus, human eyes were successfully detected and localized within the face region using Haar Cascade classifiers in OpenCV.
"""

# ==================== PROGRAM CODE ====================
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

print("RESULT: Thus, human eyes were successfully detected and localized within the face region using Haar Cascade classifiers in OpenCV.")
