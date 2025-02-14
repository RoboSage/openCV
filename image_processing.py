import cv2  # OpenCV library for image processing
import os   # OS module for handling file paths

# Define the path to read the image
image_read_path = os.path.join(".", "data", "image", "profile.png")

# Define the path to save the new image
image_write_path = os.path.join(".", "data", "image", "profile_new.png")

# Check if the image file exists at the specified path
if os.path.exists(image_read_path):
    print("✅ Image found at:", image_read_path)
else:
    print("❌ Image not found! Check the path.")

# Read the image from the file
img = cv2.imread(image_read_path)  # Load the image as a NumPy array

# Check if the image was loaded successfully
if img is None:
    print("❌ Failed to load image. Check the file path or format.")
else:
    print("✅ Image loaded successfully! Shape:", img.shape)  # Print the image dimensions (height, width, channels)

# Save the loaded image to a new file
cv2.imwrite(image_write_path, img)  # Write (save) the image to the specified location

# Define a window name for displaying the image
window_name = 'image'

# Display the image in a new window (works in general IDEs like PyCharm, VS Code, etc.)
cv2.imshow(window_name, img)

# Wait indefinitely for a key press to close the window
cv2.waitKey(0)
