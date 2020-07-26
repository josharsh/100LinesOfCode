import cv2
cap = cv2.VideoCapture()

while cap.isOpened():
    ret, back = cap.read()
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
print('done')