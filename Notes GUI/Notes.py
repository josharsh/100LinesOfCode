from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
import tkinter.scrolledtext as tkscroll
import os

root = Tk()
root.geometry("1000x600")
root.title("Notes")
action = None

def back(frame):
	if frame == 'show':
		show_frame.lower()
	if frame == 'display':
		display_frame.lower()
	title_var.set('')
	body.delete(1.0,END)

def save():
	title_text = title_var.get()
	content = body.get(1.0,END)
	save_file =	asksaveasfilename(initialfile=f'{title_text}.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
	try:
		file = open(save_file,"w+") 
		file.writelines(content)
		file.close()
	except:
		pass

def show():
	global action
	action = 'show'
	view()

def remove():
	global action 
	action = 'remove'
	view()

def view():
	tree.delete(*tree.get_children())
	files = os.listdir()
	for file in files:
		if '.txt' in file:
			file = file[:len(file)-4]
			tree.insert('',END,values=(file))
	show_frame.lift()

def OnDoubleClick(event):
	if action == 'show':
	    title = tree.set(tree.identify_row(event.y))['0']
	    files = os.listdir()
	    for file in files:
	    	if title in file:
	    		display(file)
	if action == 'remove':
		file = tree.set(tree.identify_row(event.y))['0']
		os.remove(f'{file}.txt')
		view()

def display(file):
	f = open(file,'r')
	content = f.read()
	dis_label.insert(1.0,content)
	display_frame.lift()

main_frame = Frame(root,bg='#C2C0BE')
main_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
main_frame.lift()
show_frame = Frame(root,bg='#C2C0BE')
show_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
show_frame.lower()
display_frame = Frame(root,bg='#C2C0BE')
display_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
display_frame.lower()
title_label = Label(main_frame,text="Title  :  ",font=('Calibiri', 20),bg='#BEB4AA',relief=RAISED).place(relx=0.1,rely=0.05,relwidth=0.1,relheight=0.08)
title_var = StringVar()
title = Entry(main_frame,textvariable=title_var,font=('Calibiri', 20),relief=RAISED)
title.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.08)
body = Text(main_frame,font=('Calibiri', 16),relief=RAISED)
body.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.5)
save_btn = Button(main_frame,text='Save',font=('Calibiri', 20),command=lambda: save()).place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)
show_btn = Button(main_frame,text='Show All',font=('Calibiri', 20),command=lambda: show()).place(relx=0.7,rely=0.8,relwidth=0.2,relheight=0.1)
style = ttk.Style()
style.theme_use('clam')
style.configure("mystyle.Treeview", font=('Calibri', 14), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18,'bold'))
tree = ttk.Treeview(show_frame, selectmode='browse', style="mystyle.Treeview",show=['headings'])
tree['columns'] = ('0')
tree.heading("0", text="Title")
tree.column("0", minwidth=100,width=275)
tree.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)
tree.bind("<Double-1>", OnDoubleClick)
remove_btn = Button(main_frame,text='Delete',font=('Calibiri', 20),command=lambda: remove()).place(relx=0.1,rely=0.8,relwidth=0.2,relheight=0.1)
dis_label = tkscroll.ScrolledText(display_frame,font=('Calibiri', 20),bg='#ffffff',relief=GROOVE)
dis_label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)
bact_btn_show = Button(show_frame,text='Back',font=('Calibiri', 20),command=lambda: back('show')).place(relx=0.4,rely=0.85,relwidth=0.2,relheight=0.1) 
bact_btn_show = Button(display_frame,text='Back',font=('Calibiri', 20),command=lambda: back('display')).place(relx=0.4,rely=0.85,relwidth=0.2,relheight=0.1) 
root.mainloop()