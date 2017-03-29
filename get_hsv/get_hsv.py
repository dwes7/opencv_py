# import the necessary packages
import argparse
import cv2
import pandas as pd
import numpy as np
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
    	image = clone.copy()

    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
    	break



# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    blur = cv2.medianBlur(roi, 3)
    erode = cv2.erode(blur, None, iterations=2)
    dilate = cv2.dilate(erode, None, iterations=2)
    hsv = cv2.cvtColor(dilate, cv2.COLOR_BGR2HSV)
    height, width, channels = hsv.shape

    h = np.array([None])
    s = np.array([None])
    v = np.array([None])

    print h
    print s
    print v

    print("desired length of array should be: ", width*height + 1)
    for  col in range(0, width):
        h = np.append(h ,hsv[:, col, 0])
        s = np.append(s, hsv[:, col, 1])
        v = np.append(v, hsv[:, col, 2])



    print("h", h.shape, "s", s.shape, "v", v.shape)


    hue_data = pd.DataFrame(h)
    sat_data = pd.DataFrame(s)
    val_data = pd.DataFrame(v)
    hue_data.to_csv("hue.csv")
    sat_data.to_csv("sat.csv")
    val_data.to_csv("val.csv")
    cv2.imshow("ROI", hsv)
    cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()
