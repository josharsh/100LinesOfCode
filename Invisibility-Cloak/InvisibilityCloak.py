# completed

import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)
cv2.namedWindow("Magic",cv2.WINDOW_AUTOSIZE)
img = np.zeros((600, 600, 3), np.uint8)
cv2.putText(img, "Press 'S' to continue.", (30,30), font, 1, (0,255,125))

#Getting background image.
while(True):
    cv2.imshow("Magic",img)
    ret, frame = cap.read()
    if cv2.waitKey(0) == ord('s'):
        bg = frame
        cv2.destroyWindow("Magic")
        cv2.imshow("Press 'Y' to confirm background for magic.", bg)
    if cv2.waitKey(0) == ord('y'):
        cv2.imwrite("bg.jpg",bg)
        break
    else:
        cv2.destroyWindow("Press 'Y' to confirm background for magic.")
        continue
cv2.destroyAllWindows()

#from hsv_detector.py
hl = 0          #<----INPUT----
sl = 63         #<----INPUT----
vl = 39         #<----INPUT----
hh = 28         #<----INPUT----
sh = 255        #<----INPUT----
vh = 146        #<----INPUT----

#Real "magic"
while(True):
    ret, frame = cap.read()

    #bilateral filtering (to preserve the edges)
    bfilter = cv2.bilateralFilter(frame,3,95,95)
    #cv2.imshow("Bilateral Filter",bfilter)

    #Gaussian blurring
    gblur = cv2.GaussianBlur(bfilter, (9, 9), 0)
    #cv2.imshow("Gaussian Blur", gblur)
    
    #threshing
    hsv = cv2.cvtColor(gblur, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    ran = cv2.inRange(hsv,(hl,sl,vl),(hh,sh,vh))
    #cv2.imshow("Threshold", ran)
    
    #erosion and dilation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening0 = cv2.morphologyEx(ran, cv2.MORPH_OPEN, kernel)
    closing0 = cv2.morphologyEx(opening0, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing0, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing",closing)
    thresh = closing

    #removing selected region and layering on top of previosuly saved image
    back = cv2.imread("bg.jpg", cv2.IMREAD_COLOR)
    back_res = cv2.resize(back, (frame.shape[1], frame.shape[0]), interpolation = cv2.INTER_LINEAR)
    masked_bg = cv2.bitwise_and(back, back, mask = thresh)
    masked_fg = cv2.bitwise_and(frame, frame, mask = cv2.bitwise_not(thresh))
    final = cv2.addWeighted(masked_bg, 1, masked_fg, 1, 0)

    # showing final frame
    cv2.imshow("Final", final)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()