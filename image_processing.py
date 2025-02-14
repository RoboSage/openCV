import cv2
import matplotlib.pyplot as plt
import os

image_read_path = os.path.join(".", "data","image", "profile.png")
image_write_path = os.path.join(".", "data","image", "profile_new.png")

if os.path.exists(image_read_path):
    print("✅ Image found at:", image_read_path)
else:
    print("❌ Image not found! Check the path.")

img = cv2.imread(image_read_path)

if img is None:
    print("❌ Failed to load image. Check the file path or format.")
else:
    print("✅ Image loaded successfully! Shape:", img.shape)

cv2.imwrite(image_write_path,img)

window_name = 'image'

cv2.imshow(window_name,img) #In general IDE.

cv2.waitKey(0) #For holding the image in a window.