from tkinter import *

root = Tk()
root.title('Calculator')

# define number buttons
i = 0


def get_number(x):
    global i
    i = len(display.get())
    display.insert(i, x)


# define operations
def operation(x):
    global i
    i = len(display.get())
    display.insert(i, x)


def ac():
    display.delete(0, END)


def equate():
    a = display.get()
    b = eval(a)
    ac()
    display.insert(0, b)


# define special operations
def clear1():
    a = display.get()
    b = a[:-1]
    ac()
    display.insert(0, b)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x*(factorial(x-1))


def factx():
    a = int(display.get())
    b = factorial(a)
    ac()
    display.insert(0, b)


# Create a beautiful GUI
display = Entry(root)
display.grid(row=1, columnspan=10, sticky=W+E)
Button(root, text='1', command=lambda: get_number(1)).grid(row=2, column=1)
Button(root, text='2', command=lambda: get_number(2)).grid(row=2, column=2)
Button(root, text='3', command=lambda: get_number(3)).grid(row=2, column=3)
Button(root, text='4', command=lambda: get_number(4)).grid(row=3, column=1)
Button(root, text='5', command=lambda: get_number(5)).grid(row=3, column=2)
Button(root, text='6', command=lambda: get_number(6)).grid(row=3, column=3)
Button(root, text='7', command=lambda: get_number(7)).grid(row=4, column=1)
Button(root, text='8', command=lambda: get_number(8)).grid(row=4, column=2)
Button(root, text='9', command=lambda: get_number(9)).grid(row=4, column=3)
Button(root, text='<-', command=lambda: clear1()).grid(row=5, column=1)
Button(root, text='0', command=lambda: get_number(0)).grid(row=5, column=2)
Button(root, text='=', command=lambda: equate()).grid(row=5, column=3)
Button(root, text='+', command=lambda: operation('+')).grid(row=2, column=4)
Button(root, text='-', command=lambda: operation('-')).grid(row=3, column=4)
Button(root, text='x', command=lambda: operation('*')).grid(row=4, column=4)
Button(root, text='/', command=lambda: operation('/')).grid(row=5, column=4)
Button(root, text='%', command=lambda: operation('%')).grid(row=2, column=5)
Button(root, text='^', command=lambda: operation('**')).grid(row=3, column=5)
Button(root, text='!', command=lambda: factx()).grid(row=4, column=5)
Button(root, text='AC', command=lambda: ac()).grid(row=5, column=5)
Button(root, text='pi', command=lambda: operation('*3.14')).grid(row=2, column=6)
Button(root, text='(', command=lambda: operation('(')).grid(row=3, column=6)
Button(root, text=')', command=lambda: operation(')')).grid(row=4, column=6)
Button(root, text='.', command=lambda: operation('.')).grid(row=5, column=6)


# loop
root.mainloop()
