import cv2
import numpy as np

img = cv2.imread('input.jpg')
ros, cols = img.shape[:2]

kernel_identity = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0


cv2.imshow('Orinigal', img)


output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)

ouput = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('3x3 filter', output)

ouput = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)

# You can also call output= cv2.blur(img, (3, 3)) to apply the filter
# to the image

cv2.waitKey(0)




