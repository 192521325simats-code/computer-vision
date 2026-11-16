"""
EXPERIMENT 26
Aim: Implement a function to reverse the frames of the video to create a video in reverse mode using OpenCV.
"""
import cv2
import os

def reverse_video(input_path="sample_video.mp4", output_video_path="experiment 26_output.mp4"):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Video not found at {input_path}")

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise IOError(f"Could not open video {input_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    total_frames = len(frames)
    print(f"Read {total_frames} frames from {input_path}")

    if total_frames == 0:
        raise ValueError("No frames read from video.")

    # Write frames in reverse order
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for idx, frame in enumerate(reversed(frames)):
        rev_frame = frame.copy()
        cv2.rectangle(rev_frame, (10, 10), (320, 50), (0, 0, 0), -1)
        cv2.putText(rev_frame, f"REVERSE MODE [{idx+1}/{total_frames}]", (20, 38),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 255), 2)
        out.write(rev_frame)

    out.release()
    print(f"[OK] Saved {output_video_path}")

    # Also save snapshot image preview
    if frames:
        preview = frames[-1].copy()
        cv2.putText(preview, "EXP 26: Reversed Video Frame Snapshot", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imwrite("experiment 26_output.jpg", preview)
        print("[OK] Saved experiment 26_output.jpg")

if __name__ == "__main__":
    reverse_video()
