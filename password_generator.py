from string import ascii_letters, digits, punctuation
import tkinter as tk
import random

def generator(screen, key):
    k1 = key.get()
    try:
        length = int(k1)
        a = ''.join(random.choices(digits + ascii_letters + punctuation, k=length))
        screen.delete(0, tk.END)
        screen.insert(0, a)
    except ValueError:
        screen.delete(0, tk.END)
        screen.insert(0, "Invalid length")

def display(fen):
    screen = tk.Entry(fen, border=2)
    screen.grid(row=0, column=0, columnspan=6)
    screen.pack(expand=True)
    return screen

def interface(fen):
    fen.geometry("600x400")
    screen = display(fen)
    key = tk.Entry(fen, border=2)
    key.pack(expand=True)
    button = tk.Button(fen, text="Generator", command=lambda: generator(screen, key))
    button.pack(expand=True)

if __name__ == "__main__":
    fen = tk.Tk()
    fen.resizable(False, False)
    interface(fen)
    fen.mainloop()
