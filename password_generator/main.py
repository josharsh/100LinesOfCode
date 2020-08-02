import tkinter as tk
from password_generator import PasswordGenerator

window = tk.Tk()
window.title('Password Generator')
window.geometry('400x200')

l = tk.Label(window, bg='white', width=60, text='Click on Generate to generate a password')
l.pack()


def get_password():
    display_text = PasswordGenerator().generate_random_password(lowercase=lowercase_check.get(), uppercase=uppercase_check.get(),
                                                                digits=digit_check.get(), special_characters=special_check.get())
    l.config(text=display_text)


lowercase_check = tk.BooleanVar()
uppercase_check = tk.BooleanVar()
digit_check = tk.BooleanVar()
special_check = tk.BooleanVar()

c_lowercase = tk.Checkbutton(window, text='Lowercase', variable=lowercase_check, onvalue=True, offvalue=False, command=get_password)
c_lowercase.pack()
c_uppercase = tk.Checkbutton(window, text='Uppercase', variable=uppercase_check, onvalue=True, offvalue=False, command=get_password)
c_uppercase.pack()
c_digit = tk.Checkbutton(window, text='Digits', variable=digit_check, onvalue=True, offvalue=False, command=get_password)
c_digit.pack()
c_special = tk.Checkbutton(window, text='Special Charaters', variable=special_check, onvalue=True, offvalue=False, command=get_password)
c_special.pack()

window.mainloop()