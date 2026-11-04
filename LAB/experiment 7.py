"""
EXPERIMENT 7: Video Processing (Normal, Slow Motion, and Fast Motion)
Aim:
    Perform basic video processing operations on the captured video.
    Read captured video in python and display/save the video in normal motion,
    in slow motion, and in fast motion.
"""
import cv2
import os

def process_video():
    video_path = "sample_video.mp4" if os.path.exists("sample_video.mp4") else 0
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    normal_delay = max(1, int(1000 / fps))
    slow_delay = int(normal_delay * 3)       # 3x slower delay
    fast_delay = max(1, int(normal_delay / 3)) # 3x faster delay

    print(f"Video FPS: {fps}, Dimensions: {width}x{height}, Total Frames: {total_frames}")
    print(f"Normal Delay: {normal_delay}ms | Slow Delay: {slow_delay}ms | Fast Delay: {fast_delay}ms")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Video Writers for Slow Motion and Fast Motion
    slow_out = cv2.VideoWriter("experiment 7_slow_motion.mp4", fourcc, fps, (width, height))
    fast_out = cv2.VideoWriter("experiment 7_fast_motion.mp4", fourcc, fps, (width, height))
    combined_out = cv2.VideoWriter("experiment 7_output.mp4", fourcc, fps, (width, height))

    # Read all frames into memory for flexible processing
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    print(f"Read {len(frames)} frames. Generating output videos...")

    # 1. Generate Slow Motion Video (duplicate each frame 3 times at 30 FPS => 1/3x speed)
    for idx, frame in enumerate(frames):
        slow_frame = frame.copy()
        cv2.rectangle(slow_frame, (10, 10), (330, 50), (0, 0, 0), -1)
        cv2.putText(slow_frame, "SLOW MOTION (0.33x)", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
        for _ in range(3):
            slow_out.write(slow_frame)

    slow_out.release()
    print("[OK] Saved experiment 7_slow_motion.mp4")

    # 2. Generate Fast Motion Video (sample every 3rd frame at 30 FPS => 3x speed)
    for idx in range(0, len(frames), 3):
        fast_frame = frames[idx].copy()
        cv2.rectangle(fast_frame, (10, 10), (310, 50), (0, 0, 0), -1)
        cv2.putText(fast_frame, "FAST MOTION (3.0x)", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
        fast_out.write(fast_frame)

    fast_out.release()
    print("[OK] Saved experiment 7_fast_motion.mp4")

    # 3. Generate Combined Comparison Output Video (Normal -> Slow -> Fast)
    # Part A: Normal Motion
    for frame in frames:
        f = frame.copy()
        cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
        cv2.putText(f, "NORMAL MOTION (1.0x)", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        combined_out.write(f)

    # Part B: Slow Motion
    for frame in frames:
        f = frame.copy()
        cv2.rectangle(f, (10, 10), (330, 50), (0, 0, 0), -1)
        cv2.putText(f, "SLOW MOTION (0.33x)", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 255), 2)
        for _ in range(3):
            combined_out.write(f)

    # Part C: Fast Motion
    for idx in range(0, len(frames), 3):
        f = frames[idx].copy()
        cv2.rectangle(f, (10, 10), (310, 50), (0, 0, 0), -1)
        cv2.putText(f, "FAST MOTION (3.0x)", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)
        combined_out.write(f)

    combined_out.release()
    print("[OK] Saved experiment 7_output.mp4")

    # Also save snapshot image preview
    if frames:
        sample_frame = frames[len(frames) // 2].copy()
        cv2.putText(sample_frame, "EXP 7: Video Processing (Normal, Slow, Fast)",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imwrite("experiment 7_output.jpg", sample_frame)
        print("[OK] Saved experiment 7_output.jpg")

    print("\nVideo processing complete! Output videos generated successfully.")

if __name__ == "__main__":
    process_video()
