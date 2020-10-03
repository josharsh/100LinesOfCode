import cv2
import numpy as np

#input 

cap = cv2.VideoCapture('./video.mp4') # VIDEO!! or also can be  donw with webcam
img = cv2.imread('./img.jpeg') # background img

# resizing 
# not necessary if using webcam
dim = (480, 848)
back = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# the main magic

while cap.isOpened():
    #take each frame
    ret, frame = cap.read()

    if ret:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv", hsv)

        # to get hsv value 
        red = np.uint8([[[64,30,254]]]) # bgr value of red 

        #convert to hsv 

        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #print(hsv_red)

        # threshold color values 
        l_red = np.array([165, 100, 100])   # lower value of red
        u_red = np.array([185, 255, 255])  # higher value of red



        

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        #cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        #cv2.imshow("mask", part2)

        cv2.imshow("cloak", part1 + part2)



        if cv2.waitKey(5) == ord('q'):
            break

cap.release()

cap.destroyAllWindows()