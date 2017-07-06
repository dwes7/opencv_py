import cv2
import numpy as np

img1 = cv2.imread('shapes.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

row1, cols1 = img1.shape
row2, cols2 = img2.shape

sobel_horizontal1 = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical1 = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=5)
laplacian1 = cv2.Laplacian(img1, cv2.CV_64F)

sobel_horizontal2 = cv2.Sobel(img2, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical2 = cv2.Sobel(img2, cv2.CV_64F, 0, 1, ksize=5)
laplacian2 = cv2.Laplacian(img2, cv2.CV_64F)
canny = cv2.Canny(img2, 50, 240) # Canny is the better of the filters in most cases

cv2.imshow('Original', img1)
cv2.imshow('Sobel horizonal', sobel_horizontal1)
cv2.imshow('Sobel vertical', sobel_vertical1)
cv2.imshow('Laplacian', laplacian1)

cv2.imshow('canny', canny) 
cv2.imshow('Laplacian2', laplacian2)
cv2.waitKey(0)