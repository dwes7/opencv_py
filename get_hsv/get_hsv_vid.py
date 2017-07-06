import numpy as np
import argparse
import cv2
import pandas as pd

# create argumnet parser handler
ap = argparse.ArgumentParser()
# add video camera parser to handler
ap.add_argument("-v", "--video",
                help="path to the video file")
# add buffer size to parser handler
ap.add_argument("-b", "--buffer", type=int, default=32,
                help="max buffer size")
args = vars(ap.parse_args())


# assign camera to be the input video
camera = cv2.VideoCapture(args["video"])

isFirstFrame = True

refPt = []
cropping =  False

h = np.array([None])
s = np.array([None])
v = np.array([None])
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping

    # if the left mouse button is clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        #record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False

        # draw a rectangle around the region of interest
        cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_and_crop)

isReset = False

counter = 0

while True:

    # grab the current frame
    (grabbed, frame) = camera.read()
    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    if args.get("video") and not grabbed:
        break

    # if this is the first frame pause the program and show the frame

    if isFirstFrame:
        print "use mouse to select desried area"
        clone = frame.copy()
        cv2.imshow("Frame", frame)
        cv2.waitKey(0)
        print("selected space", refPt)
    isFirstFrame = False

    clone = frame.copy()



    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break
    cv2.imshow("Frame", frame)

    counter += 1

    if len(refPt) == 2 and counter == 15:
        counter = 0
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        blur = cv2.medianBlur(roi, 3)
        erode = cv2.erode(blur, None, iterations=2)
        dilate = cv2.dilate(erode, None, iterations=2)
        hsv = cv2.cvtColor(dilate, cv2.COLOR_BGR2HSV)
        height, width, channels = hsv.shape

        for col in range(0, width):
            h = np.append(h, hsv[:, col, 0])
            s = np.append(s, hsv[:, col, 1])
            v = np.append(v, hsv[:, col, 2])

        cv2.imshow("HSV", hsv)
        cv2.waitKey(2)

# print("h", h.shape, "s", s.shape, "v", v.shape)
hue_data = pd.DataFrame(h)
sat_data = pd.DataFrame(s)
val_data = pd.DataFrame(v)
hue_data.to_csv("hue.csv")
sat_data.to_csv("sat.csv")
val_data.to_csv("val.csv")



camera.release()
cv2.destroyAllWindows()
