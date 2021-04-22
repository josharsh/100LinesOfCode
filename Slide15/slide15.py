from  tkinter import Tk,Label,Frame,Button,messagebox
import random

def click(r,c):
    if llist[r][c]['text'] == ' ':
        return

    for i in range(width):
        if llist[r][i]['text'] == ' ':
            x = i-c
            q = int(((x**2)**(1/2))/x/(-1))
            for j in range(x,0,q):
                swap(r,c+j,r,c+j+q)
            break

        elif llist[i][c]['text'] == ' ':
            x = i-r
            q = int(((x**2)**(1/2))/x/(-1))
            for j in range(x,0,q):
                swap(r+j,c,r+j+q,c)
            break

    refresh()

def refresh():
    for i in range(width):
        for j in range(width):
            llist[i][j].grid(row = i,column =j)
            llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: click(r,c))
    checkwin()

def swap(r,c,s,d):
    a = llist[r][c]
    llist[r][c] = llist[s][d]
    llist[s][d] = a

def checkwin():
    flag = 1
    for i in range(width):
        for j in range(width):
            if i != width-1 or j!=width-1:
                if llist[i][j]['text'] != i*width+j+1:
                    flag = 0
    if flag:
        messagebox.showinfo('Congradulations','YOU WIN!!')

def shuffle():
    l = []
    for i in range(width*10):#randomly sliding 100 times
        a = random.randint(0,width-1)
        b = random.randint(0,width-1)
        c = random.randint(0,width-1)
        d = random.randint(0,width-1)
        swap(a,b,c,d)

    for i in range(width):#making a linear list
        for j in range(width):
            l.append(llist[i][j]['text'])
            if llist[i][j]['text'] == ' ':
                a = width-i
            elif llist[i][j]['text'] == 1:
                a1,b1 = i,j
            elif llist[i][j]['text'] == 2:
                a2,b2 = i,j

    def inversions(l,j):
        s = 0
        for i in l:
            if i != ' ':
                if i < j and l.index(i) > l.index(j):
                    s += 1
        return(s)

    inv_count = 0
    for i in l:# counting total no. of inversions
        if i != ' ':
            inv_count += inversions(l,i)

    if width % 2 == 0:
        if inv_count%2 == 0:
            if a%2 == 0:
                swap(a1,b1,a2,b2)
        else:
            if a%2 != 0:
                swap(a1,b1,a2,b2)
    else:
        if inv_count % 2 != 0:
            swap(a1,b1,a2,b2)

def Start_Game():
    Game.mainloop()

Game = Tk()

default = 4

frame = Frame(Game)
frame.grid(row=0,column=0)

font = ('Banschrift',25)
color = '#b2babb'
width = default

llist = [[0]*width for _ in range(width)]
for i in range(width):
    for j in range(width):
        if i != width-1 or j!=width-1:
            llist[i][j] = Label(frame,text=i*width+j+1,font = font,background = color,bd = 1, relief = 'ridge',height = 2, width = 4)
        else:
            llist[i][j] = Label(frame,text=' ',font = font,background = 'white',bd = 1, relief = 'ridge',height = 2, width = 4)

shuffle()
refresh()

if __name__ == '__main__':
    Start_Game()