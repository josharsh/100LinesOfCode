#Colours

import numpy as np
import cv2

def nothing(x) :
	pass

cap = cv2.VideoCapture(0)

#hsv = cv2.cvtColor(frame,cv2.COLOR_GRAY2HSV)

cv2.namedWindow("image",cv2.WINDOW_NORMAL)

cv2.createTrackbar('Hue low','image',0,179,nothing)
cv2.createTrackbar('Sat low','image',0,255,nothing)
cv2.createTrackbar('Val low','image',0,255,nothing)
cv2.createTrackbar('Hue high','image',0,179,nothing)
cv2.createTrackbar('Sat high','image',0,255,nothing)
cv2.createTrackbar('Val high','image',0,255,nothing)
while(1) :
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	hl = cv2.getTrackbarPos('Hue low','image')
	sl = cv2.getTrackbarPos('Sat low','image')
	vl = cv2.getTrackbarPos('Val low','image')
	hh = cv2.getTrackbarPos('Hue high','image')
	sh = cv2.getTrackbarPos('Sat high','image')
	vh = cv2.getTrackbarPos('Val high','image')
	
	ran = cv2.inRange(hsv,(hl,sl,vl),(hh,sh,vh))
	
	cv2.imshow("image",ran)

	if cv2.waitKey(1) == 27 :
		break
		
cv2.destroyAllWindows()
print (hl)
print (hh)
print (sl)
print (sh)
print (vl)
print (vh)