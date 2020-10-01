print ("Press ESC to exit.")
import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
player = 'O'
game = [[1,2,3],[4,5,6],[7,8,9]]
winnerflag = 0
checkflag = 9
def getxy(x,y) :
    if x >= 0 and x < 200 :
        x = 0
    elif x >= 200 and x < 400 :
        x = 200
    else :
        x = 400
    if y >= 0 and y < 200 :
        y = 195
    elif y >= 200 and y < 400 :
        y = 395
    else :
        y = 595
    return x,y
def putgame(a,b) :
    global game
    if a == 0 and b == 195 :
        game[0][0] = player
    elif a == 200 and b == 195 :
        game[0][1] = player
    elif a == 400 and b == 195 :
        game[0][2] = player
    elif a == 0 and b == 395 :
        game[1][0] = player
    elif a == 200 and b == 395 :
        game[1][1] = player
    elif a == 400 and b == 395 :
        game[1][2] = player
    elif a == 0 and b == 595 :
        game[2][0] = player
    elif a == 200 and b == 595 :
        game[2][1] = player
    elif a == 400 and b == 595 :
        game[2][2] = player
def winner(game) :
    global winnerflag
    if game[0][0] == game[1][1] and game[1][1] == game[2][2] :
        winnerflag = 1        
    elif game[0][0] == game[0][1] and game[0][1] == game[0][2] :
        winnerflag = 1
    elif game[0][0] == game[1][0] and game[1][0] == game[2][0] :
        winnerflag = 1        
    elif game[0][1] == game[1][1] and game[1][1] == game[2][1] :
        winnerflag = 1        
    elif game[0][2] == game[1][2] and game[1][2] == game[2][2] :
        winnerflag = 1        
    elif game[1][0] == game[1][1] and game[1][1] == game[1][2] :
        winnerflag = 1        
    elif game[2][0] == game[2][1] and game[2][1] == game[2][2] :
        winnerflag = 1        
    elif game[2][0] == game[1][1] and game[1][1] == game[0][2] :
        winnerflag = 1        
    else :
        winnerflag = 0
def drawcheck(game) :
    global checkflag
    checkflag = 9
    for i in game :
        for j in i :
            if (j == 'X' or j == 'O') :
                checkflag -= 1
def place(event,x,y,flags,param) :
    global player,nx,ny
    if event == cv2.EVENT_LBUTTONDOWN :
        nx,ny = getxy(x,y)
        if player == 'O' :
            cv2.putText(img,player,(nx,ny),font,9,(255,0,0),3)
            putgame(nx,ny)
            winner(game)
            drawcheck(game)
            print(checkflag)
            if winnerflag == 1 :
                print(player + " WINS!\n\n")
            elif checkflag == 0 :
                print("Game is a draw.")
            else : 
                player = 'X' 
        else :
            cv2.putText(img,player,(nx,ny),font,9,(255,0,0),3)
            putgame(nx,ny)
            winner(game)
            drawcheck(game)
            print(checkflag)
            if winnerflag == 1 :
                print(player + " WINS!\n\n")
            elif checkflag == 0 :
                print("Game is a draw.")
            else : 
                player = 'O'
cv2.namedWindow("TTT",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("TTT",place)
img = np.zeros((600,600,3), np.uint8)
cv2.line(img,(200,0),(200,600),(0,255,0),5)
cv2.line(img,(400,0),(400,600),(0,255,0),5)
cv2.line(img,(0,200),(600,200),(0,255,0),5)
cv2.line(img,(0,400),(600,400),(0,255,0),5)
while True :
    cv2.imshow("TTT",img)
    if(cv2.waitKey(1) == 27 or winnerflag == 1 or checkflag == 0) :
        break
cv2.destroyWindow("TTT")
