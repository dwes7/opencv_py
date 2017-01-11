import cv2
import numpy
import imutils

image = cv2.imread('gate1.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edged_im = cv2.Canny(image, 200, 255)
# ratio = image.shape[0] / 500.0
# orig = image.copy()
# image = imutils.resize(image, height=500)
#
# # convert the image to grayscale, blur it, and find edges
# # in the image
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected image
print "STEP 1: Edge Detected"
cv2.imshow("Image", image)
cv2.imshow("gray", gray)
cv2.imshow("blurred", blur)
cv2.imshow("Edged", edged_im)
cv2.waitKey(0)
cv2.destroyAllWindows()