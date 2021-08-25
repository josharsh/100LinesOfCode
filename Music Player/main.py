import pygame
from pygame import mixer
from tkinter import *
import os

pygame.mixer.init()


def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
root.title('Music player project')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="aqua",fg="black",font=('arial',25),width=35)
playlist.grid(columnspan=5)

os.chdir(r'C:\Users\saich\OneDrive\Desktop\songs') #add correct location of files
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="play",command=playsong)
playbtn.config(font=('arial',25),bg="white",fg="black",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('arial',25),bg="white",fg="black",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('arial',25),bg="white",fg="black",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('arial',25),bg="white",fg="black",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

mainloop()
