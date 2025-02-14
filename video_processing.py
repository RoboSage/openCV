import os
import cv2  # OpenCV library for video processing

# Define the path to the video file
video_read_path = os.path.join(".", "data", "video", "sample.mp4")

# Open the video file using OpenCV
video = cv2.VideoCapture(video_read_path)

# Check if the video file was opened successfully
if not video.isOpened():
    print("❌ Failed to open video. Check the file path.")
    exit()  # Exit the script if the video cannot be opened

print("🎥 Playing video... Press 'q' to exit.")

# Loop to read and display frames continuously
while True:
    ret, frame = video.read()  # Read the next frame from the video

    # If ret is False, it means no more frames are available (end of video)
    if not ret:
        print("✅ End of video.")
        break  # Exit the loop

    cv2.imshow('Frame', frame)  # Display the current frame in a window

    # Wait for a short period and check if 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🚪 Exiting video playback.")
        break  # Exit the loop if 'q' is pressed

# Release the video resources and close all OpenCV windows
video.release()
cv2.destroyAllWindows()