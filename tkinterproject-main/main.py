from tkinter import *
import math


def click(event, bg="red"):
    global scvalue
    text = event.widget.cget("text")
    event.bg = bg
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    elif text == "Del":
        scvalue.get().isalnum()
        value = str.rstrip(scvalue.get()[:-1])
        scvalue.set(value)
        screen.update()

    elif text == "sqrt":
        value = math.sqrt(int(scvalue.get()))
        scvalue.set(value)
        screen.update()

    elif text == "x!":
        value = math.factorial(int(scvalue.get()))
        scvalue.set(value)
        screen.update()

    elif text == "sin":
        value = round(math.sin(math.radians(int(scvalue.get()))), 3)
        scvalue.set(value)
        screen.update()

    elif text == "cos":
        value = round(math.cos(math.radians(int(scvalue.get()))), 3)
        scvalue.set(value)
        screen.update()

    elif text == "tan":
        value = round(math.tan(math.radians(int(scvalue.get()))), 3)
        scvalue.set(value)
        screen.update()

    elif text == "sin^-1":
        value = math.degrees(math.asin(float(scvalue.get())))
        scvalue.set(value)
        screen.update()

    elif text == "cos^-1":
        value = math.degrees(math.acos(int(scvalue.get())))
        scvalue.set(value)
        screen.update()

    elif text == "tan^-1":
        value = math.degrees(math.atan(int(scvalue.get())))
        scvalue.set(value)
        screen.update()

    elif text == "x^-1":
        value = int(scvalue.get()) ** -1
        scvalue.set(value)
        screen.update()

    elif text == "x^2":
        value = int(scvalue.get()) ** 2
        scvalue.set(value)
        screen.update()

    elif text == "x^3":
        value = int(scvalue.get()) ** 3
        scvalue.set(value)
        screen.update()

    elif text == "x^(1/3)":
        value = round(int(scvalue.get()) ** (1/3))
        scvalue.set(value)
        screen.update()

    elif text == "log()":
        value = math.log(int(scvalue.get()) ** (1/3), 15)
        scvalue.set(value)
        screen.update()

    elif text == "ln()":
        value = math.log(int(scvalue.get()) ** (1/3))
        scvalue.set(value)
        screen.update()

    elif text == "pow":
        value = math.pow(int(scvalue.get()), int(scvalue.get()))
        scvalue.set(value)
        screen.update()

    elif text == "e":
        value = math.exp
        scvalue.set(value)
        screen.update()

    elif text == "pi":
        value = math.pi
        scvalue.set(value)
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
root.config(bg="black")
root.geometry("420x470")
root.title("calc")


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, bg="grey", font=" lucida 35 bold ")
screen.pack(fill=X, ipadx=8, padx=15, pady=5)

g = Frame(bg="red", colormap="new", borderwidth=150)

# row 1  ,this is the first line


f = Frame(root, bg="black")
b = Button(f, text="9", padx=28/2, pady=5, bg="grey",   font=" lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28/2, pady=5,  bg="grey",  font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=31/2, pady=5, bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image10 = PhotoImage(file="images/sin.png")
b = Button(f, image=image10, text="sin", padx=8/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image1 = PhotoImage(file="images/square_button.png")
b = Button(f, image=image1, text="x^2", padx=19/2, pady=5, bg="grey", activebackground="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

# this is the second line ,row 2


f = Frame(root, bg="black")
b = Button(f, text="6", padx=28/2, pady=5,  bg="grey",  font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28/2, pady=5, bg="grey",  font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=31/2, pady=5,  bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image9 = PhotoImage(file="images/cos.png")
b = Button(f, image=image9, text="cos", padx=1, pady=8,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image0 = PhotoImage(file="images/inverse_button.png")
b = Button(f, image=image0, text="x^-1", padx=28/2, pady=5, bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

# this is the third line ,row 3


f = Frame(root, bg="black")
b = Button(f, text="3", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28/2, pady=5, bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=26/2, pady=5,  bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image8 = PhotoImage(file="images/tan.png")
b = Button(f, image=image8, text="tan", padx=2, pady=5, bg="grey", font=" lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image4 = PhotoImage(file="images/cube_button.png")
b = Button(f, image=image4,  text="x^3", padx=28/2, pady=5, bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

# this is the fourth line ,row 4

f = Frame(root, bg="black")
b = Button(f, text=".", padx=33/2, pady=5, bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=25/3, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=31/2, pady=5,  bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image2 = PhotoImage(file="images/sinin_button.png")
b = Button(f, image=image2, text="sin^-1", padx=2, pady=2,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image5 = PhotoImage(file="images/cubert_button.png")
b = Button(f, image=image5, text="x^(1/3)", padx=28/2, pady=5, bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)


f.pack()

# this is the five  line ,row 5
f = Frame(root, bg="black")

b = Button(f, text="(", padx=32/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="c", padx=28/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=22/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=28/2, pady=5, bg="grey", fg="red", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image6 = PhotoImage(file="images/cosin_button.png")
b = Button(f, image=image6, text="cos^-1", padx=2, pady=2,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image11 = PhotoImage(file="images/sqrt_button.png")
b = Button(f, image=image11, text="sqrt", padx=1, pady=8,  bg="grey", font="lucida 18 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)


f.pack()

# this is the six line ,row 6

f = Frame(root, bg="black")

b = Button(f, text=")", padx=32/2, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="e", padx=14, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="x!", padx=10, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="Del", padx=10/2,fg="red", pady=5, bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image7 = PhotoImage(file="images/tanin.png")
b = Button(f, image=image7,  text="tan^-1", padx=2, pady=2,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

image12 = PhotoImage(file="images/xpowx.png")
b = Button(f, image=image12, text="pow", padx=15, pady=5, bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

# this is the seven  line ,row 7

f = Frame(root, bg="black")
b = Button(f, text="pi", padx=10, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text=":", padx=15, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text=" ?", padx=10, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="&", padx=14, pady=5,  bg="grey", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="log()", padx=20/2, pady=5, bg="#A9A9A9", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="ln()", padx=32/2, pady=5,  bg="#B0B0B0", font="lucida 15 bold")
b.pack(side=LEFT, padx=2, pady=2)
b.bind("<Button-1>", click)

f.pack()

g.pack()


root.mainloop()
