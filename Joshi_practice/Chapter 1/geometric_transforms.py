import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the source image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
num_rows, num_cols = img.shape[:2]
#######################################################################
#                   Image Translation
#######################################################################

translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols+ 70, num_rows110))
cv2.imshow('Translation', img_translation)
cv2.waitKey(0)
#######################################################################
#                   Image rotation
#######################################################################

# rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2),
#                                           30, 1)
# img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
# cv2.imshow('Rotation', img_rotation)
# cv2.waitKey()