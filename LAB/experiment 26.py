"""
EXPERIMENT 26: Implement a function to reverse the frames of the video to create a video in reverse mode using OpenCV.

AIM:
    To read all frames from a video stream, reverse their temporal order, and export a reversed video file using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Open the input video using cv2.VideoCapture().
    3. Read and store each consecutive video frame in a list.
    4. Retrieve video properties (FPS, frame width, frame height).
    5. Reverse the list of frames using Python list slicing (frames[::-1]).
    6. Initialize a VideoWriter object and write all reversed frames sequentially.
    7. Release resources and save a reference frame.

INPUT:
    sample.jpg (Source image)

OUTPUT:
    experiment 26_output.jpg (Output image)

RESULT:
    Thus, video frame reversal was successfully implemented to create a reversed video playback using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

cap = cv2.VideoCapture("sample_video.mp4")
frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

if frames:
    h, w = frames[0].shape[:2]
    out = cv2.VideoWriter("experiment 26_output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 20, (w, h))
    for f in reversed(frames):
        out.write(f)
    out.release()
    cv2.imwrite("experiment 26_output.jpg", frames[-1])
print("Video frame reversal complete.")

print("RESULT: Thus, video frame reversal was successfully implemented to create a reversed video playback using OpenCV.")
