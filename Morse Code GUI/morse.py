from tkinter import *
class gui:
    def __init__(self,master):
        self.master=master
        master.title("Morse Code")
        self.string=StringVar(master)
        self.result=StringVar(master)
        self.label2=Label(master,text='Enter the string: ')
        self.label2.pack()
        self.text1=Entry(master,textvariable=self.string)
        self.text1.pack()
        self.label4=Label(master,text='Select one of the options:')
        self.label4.pack()
        self.button1=Button(master,text='Encrypt',command=self.encode)
        self.button1.pack()
        self.button2=Button(master,text='Decrypt',command=self.decode)
        self.button2.pack()
        self.label3=Entry(master,textvariable=self.result)
        self.label3.pack()
        self.button3=Button(master,text='Quit',command=master.destroy)
        self.button3.pack()

    def encode(self):
        d1={' ':'|','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
        a=str(self.string.get())
        b=''
        for i in a:
            if i in d1:
                b=b+d1[i]
            b=b+' '
        self.result.set(str(b))

    def decode(self):
        d2={'|':' ','.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'}
        a=str(self.string.get())
        a=a.split(" ")
        b=''
        for i in a:
            if i in d2:
                b=b+d2[i]
        self.result.set(str(b))

root=Tk()
mygui=gui(root)
root.mainloop()
