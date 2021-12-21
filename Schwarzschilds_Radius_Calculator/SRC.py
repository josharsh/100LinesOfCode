import math
from tkinter import *

root= Tk()
root.title("Schwarzschild's Radius" )

#Frame
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

#Title
the_title = Label(frame, text="Schwarzschild's Radius Calculator", font='LKLUG')
the_title.pack()

#Subtitle
the_subtitle = Label(frame, text='Please, enter your mass in kilograms:')
the_subtitle.pack()

#Entry
mass_entry = Entry(frame,text='Enter Mass', width=50)
mass_entry.pack()

#Buttons function
def radius_calc():

	c = 299792458
	m = mass_entry.get()
	upper = int(m) * 2 * 9.8
	lower = c**2
	radius = upper/lower
	
	result = Label(frame, text=f"""
	Having a mass of {m} kilograms and
	were to reduce to {radius} meters,
	you would become a black hole.
			""")
	result.pack()


#Buttons
button_calculate = Button(frame, text='Calculate', command=radius_calc)
button_calculate.pack()

button_quit = Button(frame, text='Quit', command=root.quit)
button_quit.pack()


root.mainloop()