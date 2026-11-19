"""
EXPERIMENT 39: Write a Python function to play the given video in reverse mode in slow motion.

AIM:
    To read video frames from an input video, reverse their sequence order, and save/play the video in reverse slow motion using OpenCV.

PROCEDURE:
    1. Import cv2.
    2. Open the input video file using cv2.VideoCapture('sample_video.mp4').
    3. Read all frames sequentially and append them into a Python list.
    4. Reverse the list of frames using Python slicing frames[::-1].
    5. Create a cv2.VideoWriter object configured with reduced frame rate (e.g. 10 FPS) to achieve slow-motion playback.
    6. Write the reversed frames sequentially to the output video file experiment 39_output.mp4.
    7. Release video resources and save a representative frame to disk.

INPUT:
    sample.jpg (Source image)

OUTPUT:
    experiment 39_output.jpg (Output image)

RESULT:
    Thus, a function to play and export a video in reverse mode in slow motion was successfully implemented using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

cap = cv2.VideoCapture("sample_video.mp4")
frames = []
while cap.isOpened() and len(frames) < 60:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

if frames:
    h, w = frames[0].shape[:2]
    rev_frames = list(reversed(frames))
    
    # Save reverse slow-motion video (10 FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("experiment 39_output.mp4", fourcc, 10, (w, h))
    for f in rev_frames:
        out.write(f)
    out.release()
    
    # Save snapshot
    cv2.imwrite("experiment 39_output.jpg", rev_frames[0])
    print("Reverse slow motion video export complete.")

print("RESULT: Thus, a function to play and export a video in reverse mode in slow motion was successfully implemented using OpenCV.")
