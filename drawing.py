import cv2  # OpenCV library for image processing
import os   # OS module for handling file paths

image_read_path = os.path.join(".", "data", "image", "whiteboard.jpg")  # "." represents the current directory

img = cv2.imread(image_read_path)  # Load the image as a NumPy array. Returns None if the image can't be read.

if img is not None: # Check if the image was loaded successfully
    # line
    cv2.line(img, (100, 100), (400, 400), (0, 255, 0), 3) # (0,255,0) is green, 3 is the thickness.

    # rectangle
    cv2.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 3) # (0,0,255) is blue, 3 is the thickness.

    # circle
    cv2.circle(img, (250, 250), 80, (255, 0, 0), 3) # (250, 250) is the center, 80 is the radius, (255, 0, 0) is red, 3 is the thickness.

    # text
    font = cv2.FONT_HERSHEY_SIMPLEX # Choose a font
    cv2.putText(img, 'OpenCV Drawing', (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA) # Add text to the image.

    window_name = 'Original Image with Drawings'  # More descriptive name

    # Display the original image in a new window. cv2.imshow needs cv2.waitKey() to function properly.
    cv2.imshow(window_name, img)

    # Wait indefinitely for a key press to close the window. This is essential for the cv2.imshow() to work.
    # 0 means wait indefinitely. You can also specify a time in milliseconds.
    cv2.waitKey(0)  # Waits for any key press. You could use cv2.waitKey(1) to wait 1ms and continue the loop for video processing.

    # Destroy all windows. This is good practice to release resources.
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not read the image from {image_read_path}") # print an error if the image could not be loaded.