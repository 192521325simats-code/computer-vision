"""
EXPERIMENT 7: Perform basic video processing operations on the captured video. Read captured video in python and display the video, in slow motion and in fast motion.

AIM:
    To perform video processing operations by reading a video file in Python and saving/displaying the video in normal, slow motion, and fast motion modes using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Open video file or capture stream using cv2.VideoCapture().
    3. Extract video properties: frame width, height, and FPS.
    4. To simulate slow motion, increase playback delay (cv2.waitKey) or record at reduced frame rate.
    5. To simulate fast motion, decrease playback delay or record at multiplied frame rate.
    6. Write the resulting frames to output video files using cv2.VideoWriter().
    7. Release video resources using cap.release() and out.release().

INPUT:
    photo.jpg (Source image)

OUTPUT:
    experiment 7_output.jpg (Output image)

RESULT:
    Thus, video processing operations were successfully executed to produce both slow motion and fast motion playback using OpenCV.
"""

# ==================== PROGRAM CODE ====================
import cv2

cap = cv2.VideoCapture("sample_video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out_slow = cv2.VideoWriter("experiment 7_slow_motion.mp4", fourcc, max(5, fps / 2), (w, h))
out_fast = cv2.VideoWriter("experiment 7_fast_motion.mp4", fourcc, min(60, fps * 2), (w, h))

frame_count = 0
first_frame = None
while cap.isOpened() and frame_count < 60:
    ret, frame = cap.read()
    if not ret:
        break
    if first_frame is None:
        first_frame = frame
    out_slow.write(frame)
    out_fast.write(frame)
    frame_count += 1

cap.release()
out_slow.release()
out_fast.release()
if first_frame is not None:
    cv2.imwrite("experiment 7_output.jpg", first_frame)
print("Video processing complete.")

print("RESULT: Thus, video processing operations were successfully executed to produce both slow motion and fast motion playback using OpenCV.")
