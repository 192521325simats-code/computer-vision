"""
EXPERIMENT 7: Video Processing (Normal, Slow Motion, and Fast Motion)

AIM:
    To perform basic video processing operations on a captured video: read captured video in Python and display/save the video in normal motion, slow motion, and fast motion using OpenCV.

PROCEDURE:
    1. Import cv2 and os modules.
    2. Open the video source using cv2.VideoCapture().
    3. Retrieve video properties including FPS, frame width, and frame height.
    4. Normal Motion: Process and write frames at native frame delay (1000 / fps).
    5. Slow Motion: Duplicate frames / increase delay interval (3x) to achieve 0.33x playback speed.
    6. Fast Motion: Subsample frames / decrease delay interval to achieve 3.0x fast motion playback.
    7. Export video files (experiment 7_slow_motion.mp4, experiment 7_fast_motion.mp4, experiment 7_output.mp4).

INPUT:
    sample_video.mp4 (Captured video file)

OUTPUT:
    experiment 7_output.mp4, experiment 7_slow_motion.mp4, experiment 7_fast_motion.mp4, experiment 7_output.jpg

RESULT:
    Thus, basic video processing operations were successfully performed to process and display video in normal, slow, and fast motion modes.
"""

# ==================== PROGRAM CODE ====================
import cv2
import os

video_path = "sample_video.mp4" if os.path.exists("sample_video.mp4") else 0
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise IOError(f"Cannot open video: {video_path}")

fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
slow_out = cv2.VideoWriter("experiment 7_slow_motion.mp4", fourcc, fps, (width, height))
fast_out = cv2.VideoWriter("experiment 7_fast_motion.mp4", fourcc, fps, (width, height))
combined_out = cv2.VideoWriter("experiment 7_output.mp4", fourcc, fps, (width, height))

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

# 1. Slow Motion Video (duplicate each frame 3 times at 30 FPS => 0.33x speed)
for frame in frames:
    slow_frame = frame.copy()
    cv2.rectangle(slow_frame, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(slow_frame, "SLOW MOTION (0.33x)", (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    for _ in range(3):
        slow_out.write(slow_frame)
slow_out.release()
print("[OK] Saved experiment 7_slow_motion.mp4")

# 2. Fast Motion Video (sample every 3rd frame at 30 FPS => 3x speed)
for idx in range(0, len(frames), 3):
    fast_frame = frames[idx].copy()
    cv2.rectangle(fast_frame, (10, 10), (310, 50), (0, 0, 0), -1)
    cv2.putText(fast_frame, "FAST MOTION (3.0x)", (20, 38),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
    fast_out.write(fast_frame)
fast_out.release()
print("[OK] Saved experiment 7_fast_motion.mp4")

# 3. Combined Output Video (Normal -> Slow -> Fast)
for frame in frames:
    f = frame.copy()
    cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(f, "NORMAL MOTION (1.0x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    combined_out.write(f)

for frame in frames:
    f = frame.copy()
    cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
    cv2.putText(f, "SLOW MOTION (0.33x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
    for _ in range(3):
        combined_out.write(f)

for idx in range(0, len(frames), 3):
    f = frames[idx].copy()
    cv2.rectangle(f, (10, 10), (310, 50), (0, 0, 0), -1)
    cv2.putText(f, "FAST MOTION (3.0x)", (20, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
    combined_out.write(f)
combined_out.release()
print("[OK] Saved experiment 7_output.mp4")

# Save image preview
if frames:
    sample_frame = frames[len(frames) // 2].copy()
    cv2.imwrite("experiment 7_output.jpg", sample_frame)
    print("[OK] Saved experiment 7_output.jpg")

print("RESULT: Thus, basic video processing operations were successfully performed to process and display video in normal, slow, and fast motion modes.")
