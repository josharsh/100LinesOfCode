from tkinter import *
import time
import pyaudio
import numpy as np
import wave
class virtualizer(object):
     def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.canvas = Canvas(self.root, width=520, height = 400,bg='black')
        self.canvas.pack()  
        self.items=[]
        for i in range(50) :
            self.items.append(self.canvas.create_rectangle(10+10*i, 375, 20+10*i, 375, fill="blue"))
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
     def animation(self):
        track = 0
        CHUNK =1024
        RATE = 44100
        filename = 'your wav file here'
        wf = wave.open(filename)
        w= wave.open(filename)
        p=pyaudio.PyAudio()
        #stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)# get sound from mic
        stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),  channels = wf.getnchannels(),rate=wf.getframerate(),output=True)
        peak=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        a= "a"
        while a!= "nan" :
        #print(wf.getframerate())# get sound from mic
        #while True:# get sound from mic
            #datas=stream.read(CHUNK)# get sound from mic
            datas= wf.readframes(CHUNK)
            datab =  np.fromstring(datas,dtype=np.int16)
            peak1=   np.average(np.abs(datab))
            a= str((20*peak1/2**14))
            if(a!='nan' ):
                peak.pop(0)
                peak.append(peak1) 
                for i in range(50):
                    self.canvas.coords(self.items[i],10+i*10,375,20+i*10,375-10*int((20*peak[i]/2**14)))
                self.canvas.update()
            stream.write(datas)  
        else : print("finish")
        stream.stop_stream()
        stream.close()
        p.terminate()
virtualizer()
