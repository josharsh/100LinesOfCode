import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = '\Images'
images = []
class_names = []

for user_image in os.listdir(path):
    images.append(cv2.imread(user_image))
    class_names.append(user_image.split('.')[0])

def encoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeImages = encoding(images)

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        nameList = []
        dataList = f.readlines()
        for line in dataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    faceLocInFrame = face_recognition.face_locations(img)
    encodeInFrame = face_recognition.face_encodings(img, faceLocInFrame)
    
    for encodeFace, faceLoc in zip(encodeInFrame, faceLocInFrame):
        matches = face_recognition.compare_faces(encodeImages, encodeFace)
        faceDist = face_recognition.face_distance(encodeImages, encodeFace)
        
        matchIndex = np.argmin(faceDist)
        
        if matches[matchIndex]:
            name = class_names[matchIndex].upper()
            y1,x2,y2,x1 = faceLoc
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.rectangle(img,(x1,y2-35), (x2,y2), (255,0,0), cv2.FILLED)
            cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
            markAttendance(name)
            
    cv2.imshow('Face Recognition',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
