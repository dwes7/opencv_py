import cv2
import numpy as np


input_image = cv2.imread('fishing_tower.png')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray_image, None)

input_image = cv2.drawKeypoints(gray_image, keypoints, input_image)

cv2.imshow('SIFT features', input_image)
cv2.waitKey()
