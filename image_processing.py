import cv2  # OpenCV library for image processing
import os   # OS module for handling file paths
import numpy as np

# Define the path to read the image
# os.path.join helps create platform-independent paths (works on Windows, macOS, Linux)
image_read_path = os.path.join(".", "data", "image", "profile.png")  # "." represents the current directory

# Define the path to save the new image
image_write_path = os.path.join(".", "data", "image", "profile_new.png")

# Check if the image file exists at the specified path
if os.path.exists(image_read_path):
    print("✅ Image found at:", image_read_path)
else:
    print("❌ Image not found! Check the path.")
    exit() # Exit the script if the image isn't found, prevents errors later

# Read the image from the file
img = cv2.imread(image_read_path)  # Load the image as a NumPy array.  Returns None if the image can't be read.

# Check if the image was loaded successfully
if img is None:
    print("❌ Failed to load image. Check the file path or format. Supported formats include: .bmp, .jpg, .jpeg, .png, .tiff, etc.")
else:
    print("✅ Image loaded successfully! Shape:", img.shape)  # Print the image dimensions (height, width, channels).  Channels are typically 3 for color images (BGR) and 1 for grayscale.


'''
# Save the loaded image to a new file. This creates a copy.
cv2.imwrite(image_write_path, img)  # Write (save) the image to the specified location.  The format is determined by the file extension.
'''


# Define a window name for displaying the image
window_name = 'Original Image' # More descriptive name

# Display the original image in a new window.  cv2.imshow needs cv2.waitKey() to function properly.
cv2.imshow(window_name, img)


'''
# Resize the image.  (width, height) is the order of the tuple.
resized_img = cv2.resize(img, (640, 480))  # Resize to 640 pixels wide and 480 pixels high.

# Display the resized image in different window.
resized_window_name = 'Resized Image' # Distinct window name

cv2.imshow(resized_window_name, resized_img) # The same window is reused
'''


'''
# Crop the image.  Image slicing in NumPy arrays is done as [row_start:row_end, col_start:col_end].
# Remember that image coordinates start at (0, 0) in the top-left corner.
# row_start:row_end defines the vertical cropping (height).
# col_start:col_end defines the horizontal cropping (width).
cropped_img = img[220:740, 320:940]  # Crop from row 220 to 740 and column 320 to 940.

cropped_window_name = 'Cropped Image'  # Distinct window name for the cropped image.
cv2.imshow(cropped_window_name, cropped_img)  # Display the cropped image in its own window.
'''



'''
# Convert the image from BGR (Blue, Green, Red - OpenCV's default color format) to RGB (Red, Green, Blue).
# This is often necessary because other libraries and applications (like Matplotlib) expect RGB format.
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

img_rgb_window_name = 'RBG Image'  # Create a name for the window displaying the RGB image.
cv2.imshow(img_rgb_window_name, img_rgb)  # Display the RGB image in its own window.
'''



''' 
# Blurring operation on Images
# Define the kernel size for the blurring operation.
# The kernel is a small matrix (like a window) that slides over the image.
# The size of the kernel determines the amount of blurring. Larger kernel = more blur.
# For a standard box blur, the kernel size should generally be a positive and odd integer (e.g., 3, 5, 7, etc.).
k_size = 9

# Apply a box blur (also known as an averaging blur) to the image.
# The kernel size is provided as a tuple (width, height). In this case, it's a 10x10 kernel.
# A box blur calculates the average pixel value within the kernel area and replaces the center pixel with that average.
img_blur = cv2.blur(img, (k_size, k_size))  

# Apply a Gaussian blur to the image.
# Gaussian blur uses a Gaussian kernel (a bell-shaped curve) for blurring.
# It's generally more effective at reducing high-frequency noise than a box blur.
# The third argument (sigma) controls the amount of blurring. A higher sigma value results in more blur.
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 3)  # Kernel size and sigma value.

# Apply a median blur to the image.
# Median blur replaces each pixel with the median pixel value in the kernel area.
# It's particularly effective at removing salt-and-pepper noise (random black and white pixels).
# The kernel size must be an odd integer.
img_median_blur = cv2.medianBlur(img, k_size)  # Kernel size (must be odd).  k_size will be automatically converted to the next lower odd number if it's even.

img_blur_window_name = 'Blur Image'  # Create a string variable to store the name of the window.
cv2.imshow(img_blur_window_name, img_blur)  # Display the blurred image.

img_gaussian_blur_window_name = 'Gaussian Blur Image' # Create a string variable to store the name of the window.
cv2.imshow(img_gaussian_blur_window_name, img_gaussian_blur)  # Display the Gaussian blurred image.

img_median_blur_window_name = 'Median Blur Image'  # Create a string variable to store the name of the window.
cv2.imshow(img_median_blur_window_name, img_median_blur)  # Display the median blurred image.
'''



''' 
# Convert the image to grayscale.  Grayscale images have only one channel (intensity).
# This simplifies many image processing operations.
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply simple thresholding to the grayscale image.
# Thresholding converts the image to a binary image (black and white) based on a threshold value.
# Pixels with intensity below the threshold are set to one value (e.g., 0 - black), and pixels above the threshold are set to another value (e.g., 255 - white).
# cv2.threshold() returns two values:
#   - ret: The threshold value that was actually used (sometimes it's adjusted).
#   - thresh: The thresholded (binary) image.
ret, thresh1 = cv2.threshold(img_grey, 80, 255, cv2.THRESH_BINARY)  # Threshold at 80, max value 255, using binary thresholding.

threshold_window_name1 = 'Threshold Window 1'  # Create a name for the simple thresholded image window.

cv2.imshow(threshold_window_name1, thresh1)  # Display the *simple thresholded* image.

# Apply adaptive thresholding to the grayscale image.
# Adaptive thresholding calculates the threshold for small regions of the image.
# This is useful when the image has varying lighting conditions.
# cv2.adaptiveThreshold() takes several parameters:
#   - src: The source image (grayscale).
#   - maxValue: The maximum value to assign to pixels that exceed the threshold.
#   - adaptiveMethod: The adaptive thresholding method to use (e.g., cv2.ADAPTIVE_THRESH_GAUSSIAN_C).
#   - thresholdType: The thresholding type (e.g., cv2.THRESH_BINARY).
#   - blockSize: The size of the neighborhood area used for calculating the threshold. Must be an odd number.
#   - C: A constant subtracted from the mean or weighted mean.
thresh2 = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)  # Adaptive thresholding with Gaussian method, blockSize 21, and C 30.

threshold_window_name2 = 'Threshold Window 2'  # Create a name for the adaptive thresholded image window.

cv2.imshow(threshold_window_name2, thresh2)  # Display the *adaptive thresholded* image.
'''



''' 
# Apply the Canny edge detection algorithm.
# Canny edge detection is a multi-stage algorithm used to detect a wide range of edges in images.
# It uses a multi-stage algorithm to detect a wide range of edges in images.
# cv2.Canny() takes several parameters:
#   - image: The input image (grayscale or color).
#   - threshold1: The lower threshold for hysteresis procedure.
#   - threshold2: The upper threshold for hysteresis procedure.
# The algorithm finds edges with intensity gradient more than threshold2 and edges with intensity gradient less than threshold1 are suppressed.
# Edges lying between these two thresholds are either classified as edges or non-edges based on their connectivity.
img_edge = cv2.Canny(img, 50, 200)  # Apply Canny with lower threshold 100 and upper threshold 200.

canny_window_name = 'Canny Window'  # Create a name for the Canny edge detection window.

cv2.imshow(canny_window_name, img_edge)  # Display the Canny edge detected image.

# Dilate the edges to make them thicker.
# cv2.dilate() is used to apply dilation, a morphological operation.
# Dilation adds pixels to the boundaries of objects in an image.
# It takes the source image and a structuring element (kernel) as input.
# Here, a 3x3 kernel of ones is used, effectively expanding the white regions (edges).
img_edge_d = cv2.dilate(img_edge, np.ones((3,3), dtype=np.uint8)) #dilate the canny edge image.

dilate_window_name = 'Dilate Window' # create a name for the dilate window.

cv2.imshow(dilate_window_name, img_edge_d) # display the dilated edge image.

# Erode the dilated edges to make them thinner.
# cv2.erode() is used to apply erosion, a morphological operation.
# Erosion removes pixels on object boundaries.
# It takes the source image and a structuring element (kernel) as input.
# Here, a 3x3 kernel of ones is used, effectively shrinking the white regions (edges).
img_edge_e = cv2.erode(img_edge_d, np.ones((3,3), dtype=np.uint8))

erode_window_name = 'Erode Window'

cv2.imshow(erode_window_name, img_edge_e)
'''


# Wait indefinitely for a key press to close the window.  This is essential for the cv2.imshow() to work.
# 0 means wait indefinitely.  You can also specify a time in milliseconds.
cv2.waitKey(0)  # Waits for any key press.  You could use cv2.waitKey(1) to wait 1ms and continue the loop for video processing.

# Destroy all windows. This is good practice to release resources.
cv2.destroyAllWindows()