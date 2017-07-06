import cv2

cap = cv2.VideoCapture(0)

# check if the webcam is opened correctly
if not cap.isOpened():
	raise IOError("Cannon open webcam")

while True:
	ret, frame = cap.read()
	frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
	cv2.imshow('input', frame)

	c = cv2.waitKey(1) # press esc key
	if c == 27:
		break
cap.release()
cv2.destroyAllWindows()
