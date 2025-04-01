from tkinter import *
import customtkinter  # type: ignore

# Implementation
class Caesar_CipherImp:
    def __init__(self, text, shift) -> None:
        self.text = text
        self.shift = shift

    @staticmethod
    def caesar_cipher(text, shift):
        return ''.join(
            chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else
            chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char
            for char in text)

# UI
class Caesar_Cipher:
    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.configure(background='#353839')
        self.top.geometry('600x500')
        self.top.title("Caesar Cipher Encoding-Decoding")
        self.top.resizable(False, False)
        self.top.protocol("WM_DELETE_WINDOW", self.quit)

        self.decryption_result_label = None
        self.encryption_result_label = None

        self.create_widgets()

    def create_widgets(self):
        # Decryption Section
        self.create_label("Enter Text encrypted with caesar cipher:", 150, 10)
        self.caesar_input_entry = self.create_entry(50, 45)
        self.create_label("Enter shift:", 435, 10)
        self.caesar_shift_entry = self.create_entry(470, 45, width=80)
        self.create_button("Decrypt", self.process_cipher, 225, 110, decryption=True)

        # Encryption Section
        self.create_label("Enter Text:", 225, 220)
        self.text_input_entry = self.create_entry(50, 255)
        self.create_label("Enter shift:", 435, 220)
        self.text_shift_entry = self.create_entry(470, 255, width=80)
        self.create_button("Encrypt", self.process_cipher, 225, 320, decryption=False)

    def create_label(self, text, x, y):
        label = customtkinter.CTkLabel(self.top, width=150, height=30, bg_color='#353839', text_color='white', text=text)
        label.place(x=x, y=y)

    def create_entry(self, x, y, width=400):
        entry = customtkinter.CTkEntry(self.top, width=width, height=50, border_color='silver')
        entry.place(x=x, y=y)
        return entry

    def create_button(self, text, command, x, y, decryption=False):
        button = customtkinter.CTkButton(self.top, text=text, width=140, height=28, corner_radius=25)
        button.place(x=x, y=y)
        button.configure(command=lambda: command(decryption))

    def process_cipher(self, decryption=False):
        input_text = self.caesar_input_entry.get() if decryption else self.text_input_entry.get()
        shift = int(self.caesar_shift_entry.get() if decryption else self.text_shift_entry.get())
        shift = shift if not decryption else -shift
        result = Caesar_CipherImp.caesar_cipher(input_text, shift)

        result_text = "Decrypted text: " if decryption else "Encrypted text: "

        if decryption:
            if self.decryption_result_label:
                self.decryption_result_label.destroy()  # Clear previous result
            self.decryption_result_label = customtkinter.CTkLabel(self.top, width=300, height=30, bg_color='#353839',
                                                                  text_color='white', text=result_text + result)
            self.decryption_result_label.place(x=150, y=150)
        
        else:
            if self.encryption_result_label:
                self.encryption_result_label.destroy()  # Clear previous result
            self.encryption_result_label = customtkinter.CTkLabel(self.top, width=300, height=30, bg_color='#353839',
                                                                  text_color='white', text=result_text + result)
            self.encryption_result_label.place(x=150, y=350)

    def quit(self):
        root.quit()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = Caesar_Cipher(root)
    root.mainloop()