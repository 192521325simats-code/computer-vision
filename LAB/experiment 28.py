"""
EXPERIMENT 28
Aim: Implement a vehicle detection algorithm using OpenCV to detect and locate vehicles in each frame of the video.
"""
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

# Video writer for vehicle detection video output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("experiment 28_output.mp4", fourcc, fps, (width, height))

first_detected_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask = bg_subtractor.apply(frame)

    # Morphological operations to filter noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_DILATE, kernel)

    # Find contours representing moving vehicles
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
    # Fallback preview
    fallback = cv2.imread("photo.jpg") if os.path.exists("photo.jpg") else frame
    cv2.imwrite("experiment 28_output.jpg", fallback)
