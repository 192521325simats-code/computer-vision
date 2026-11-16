"""
EXPERIMENT 30: Human Smile Detection Algorithm

AIM:
    To implement a Smile detection algorithm using OpenCV to detect and locate human smile in the images.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Load pre-trained Haar Cascade classifiers for face and smile (haarcascade_smile.xml).
    3. Read the input image and convert to grayscale.
    4. Detect faces to locate the head region.
    5. Extract the lower facial region (mouth ROI) where smiles occur.
    6. Apply smile cascade detector within the mouth ROI.
    7. Draw green bounding rectangles around detected smile regions and label them.
    8. Save and display the smile detection output image.

INPUT:
    face.jpg (Input portrait image)

OUTPUT:
    experiment 30_output.jpg (Smile detected image)

RESULT:
    Thus, human smile was successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.
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

print("RESULT: Thus, human smile was successfully detected and localized in the image using Haar Cascade classifiers in OpenCV.")
