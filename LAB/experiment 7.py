"""
EXPERIMENT 7
Aim: Perform basic video processing operations on the captured video. Read captured video in python and display the video, in slow motion and in fast motion.
"""
import cv2
import os

video_path = "sample_video.mp4" if os.path.exists("sample_video.mp4") else 0
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0

normal_delay = int(1000 / fps)
slow_delay = int(normal_delay * 3)
fast_delay = max(1, int(normal_delay / 3))

# Capture sample frame for output representation
ret, frame = cap.read()
if ret:
    cv2.putText(frame, "Video Frame Preview", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imwrite("experiment 7_output.jpg", frame)
    print("[OK] Saved experiment 7_output.jpg")

cap.release()
print(f"Normal Delay: {normal_delay}ms | Slow Delay: {slow_delay}ms | Fast Delay: {fast_delay}ms")
