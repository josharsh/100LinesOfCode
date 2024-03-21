import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from datetime import datetime

HOST='127.0.0.1'
PORT= 9090
#THis is client class
class Client:
    def __init__(self,host,port):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg=tkinter.Tk()
        msg.withdraw()

        #THe following code creates a dialogbox which takes the login name of the user.
        self.name=simpledialog.askstring("Name","Enter Login Name(NOTE : This name is visible to all memebers of chat room)",parent=msg)
        self.gui_donee=False
        self.running=True

        #put gui_loop and receive in different threads and start running parallely , it is because both function will run forever.
        gui_thread=threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()
    def text_area_reset(self,message):#resets the input text area for new input and puts the message to text area

        self.text_area.config(state='normal')
        self.text_area.insert('end', message)
        self.text_area.yview('end')
        self.text_area.config(state='disabled')

    def gui_loop(self):#This function makes UI including text areas,input_area and button
        self.win=tkinter.Tk()
        self.win.title('ChatRoom')
        self.win.configure(bg="lightblue")

        self.chat_label = tkinter.Label(self.win, text=self.name.upper(), bg="lightblue")
        self.chat_label.config(font=("Arial", 14))
        self.chat_label.pack(padx=29, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win, bg="white",height=10)
        self.text_area.pack(padx=20, pady=5)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        message=f"SERVER : you joined the server at {current_time}!\n"
        self.text_area_reset(message)
        self.msg_label=tkinter.Label(self.win,text="Message:\t\t\t\t\t\t\t      ",bg="lightblue")
        self.msg_label.config(font=("Arial",14))
        self.msg_label.pack(padx=20,pady=5)

        self.input_area=tkinter.Text(self.win,height=1,width=60)
        self.input_area.config(font=("Arial", 14))
        self.input_area.pack(padx=20,pady=5)
        self.input_area.bind('<Return>', lambda _: self.write())#This function call self.write if user press enter

        self.send_button = tkinter.Button(self.win, text=" ⏩ ", command=self.write)
        self.send_button.config(font=("Arial", 14))
        self.send_button.pack(padx=20, pady=5)

        self.gui_donee=True
        self.win.protocol("WM_DELETE_WINDOW",self.kill)
        self.win.mainloop()


    def write(self):#This function forwards the input text by client to server.
        message=f"{self.name.upper()}: {self.input_area.get('1.0','end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')

    def kill(self):#kill the client
        self.running=False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):#This function receives all messages sent by server.
        while self.running:
            try:
                message=self.sock.recv(1024).decode('utf-8')
                if message=='SERVER_CHECK':#This is to ensure that connection established successfully.
                    self.sock.send(self.name.encode('utf-8'))

                else:
                    if self.gui_donee:#This is neccesary because both receive and gui_loop are running in different threads
                        self.text_area_reset(message)
            except ConnectionAbortedError:
                break
            except:
                print("Unwanted Error")
                self.sock.close()
                break
                
client=Client(HOST,PORT)#Make a client object
