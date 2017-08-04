import cv2
import numpy as np

color_image = cv2.imread('robot_arm.png')
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
fast = cv2.FastFeatureDetector_create()
gray_image_copy = gray_image.copy()
# Detect keypoints
keypoints = fast.detect(gray_image, None)
print "Number of keypoints with non max suppression: ", len(keypoints)

# Dray keypoints on top of the input input_image

img_keypoints_with_nonmax = cv2.drawKeypoints(gray_image, keypoints, color_image)
cv2.imshow('FAST keypoints - with non max suppression', img_keypoints_with_nonmax)

# Disable nonmaxSupprssion
fast.setBool('nonmaxSuppression', False)

# Detect keypoints again
keypoints = fast.detect(gray_image, None)
print "Total Keypoints without nonmaxSuppression: ", len(keypoints)

# Draw keypoints on top of the input image
img_keypoints_without_nonmax = cv2.drawKeypoints(gray_image, keypoints, color=(0, 255, 0))
cv2.imshow('Fast keypoints - without non max suppression', img_keypoints_without_nonmax)
cv2.waitKey()
