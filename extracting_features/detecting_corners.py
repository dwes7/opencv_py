import cv2
import numpy as np

img = cv2.imread('box_corners.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_copy = img.copy()
gray = np.float32(gray)

# to detect only sharp corners
dst = cv2.cornerHarris(gray, 4, 5, 0.04)
corners = cv2.goodFeaturesToTrack(gray, 7, 0.05, 25)
corners = np.float32(corners)

for item in corners:
    x, y = item[0]
    cv2.circle(img_copy, (x,y), 5, 255, -1)

# to detect soft cornerHarris
# dst = cv2.cornerHaris(gray, 14, 5, 0.04)

# Resuly is dilated for marking the corners
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image
img[dst > 0.01*dst.max()] = [0, 0, 0]

cv2.imshow('Harris Corners', img)
cv2.imshow("Top 'k' features", img_copy)
cv2.waitKey()
