import cv2  # OpenCV library for image processing
import os   # OS module for handling file paths

image_read_path = os.path.join(".", "data", "image", "birds.jpg")  # "." represents the current directory

img = cv2.imread(image_read_path)  # Load the image as a NumPy array.  Returns None if the image can't be read.

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)
        x1, y1, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x1, y1), (x1+w, y1+h), (0, 255, 0), 2)

window_name = 'Image' # More descriptive name

# Display the original image in a new window.  cv2.imshow needs cv2.waitKey() to function properly.
cv2.imshow(window_name, img)

cv2.waitKey(0)  # Waits for any key press.  You could use cv2.waitKey(1) to wait 1ms and continue the loop for video processing.

# Destroy all windows. This is good practice to release resources.
cv2.destroyAllWindows()