import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Primeiro conjunto representa a autura vertical,  0 = parte superior, 400 = parte inferior

    # Coloca em gray scale 
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # APlica threshold, variavel "_" para n ter q importar a herança, variavel nula
    _, threshold = cv2.threshold(cinza, 100, 200, type=cv2.THRESH_BINARY)

    # Cria o kernel
    kernel = np.ones((5,5),np.uint8)

    # Aplica o efeito de dilatação da camera
    dilation = cv2.dilate(threshold, kernel, iterations = 2)

    # Achando os contornos
    counturns,_ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Calculando o contorno e aplicando no frame
    for (i, c) in enumerate(counturns):
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 225, 0), 2)
        # Calculando os CM
        cmY = (h*15)/120
        cmX = (w*10)/71   
        # Mostrando na tela 
        cv2.putText(frame, str(int(cmY)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
        cv2.putText(frame, str(int(cmX)), (x+w+15, y), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)

    #Mostrando a imagem na tela
    cv2.imshow("frame", frame)
    cv2.imshow('teste', dilation)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.realese()
cv2.destroyAllWindows()