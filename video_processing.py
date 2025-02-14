import os
import cv2
import matplotlib.pyplot as plt

# Define the path to the video file
video_read_path = os.path.join(".", "data", "video", "sample.mp4")

# Open the video file
video = cv2.VideoCapture(video_read_path)

# Check if the video file was opened successfully
if not video.isOpened():
    print("❌ Failed to open video. Check the file path.")
    exit()

print("🎥 Playing video... Press 'q' to exit.")

while True:
    ret, frame = video.read()  # Read the next frame

    if not ret:
        print("✅ End of video.")
        break  # Exit loop if no more frames are available

    cv2.imshow('Frame', frame)  # Display the current frame

    # Press 'q' to exit the video playback
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🚪 Exiting video playback.")
        break

# Release the video resources and close all windows
video.release()
cv2.destroyAllWindows()
