# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
camera = cv2.VideoCapture(0)

while True:

	# load the image, clone it for output, and then convert it to grayscale
	(grabbed, frame) = camera.read()

	if not grabbed:
		break

	output = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100, 20, 100)

	print circles




	# ensure at least some circles were found
	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")

		# loop over the (x, y) coordinates and radius of the circles
		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1) 
	# show the frame and record if a key is pressed
	cv2.imshow("Frame", frame)
	cv2.imshow("output", output)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
	    break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()