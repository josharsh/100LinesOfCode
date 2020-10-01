from tkinter import *
import tkinter.font as tk_font
from tkinter.filedialog import asksaveasfile


class Note(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.m = Menu(self, tearoff=0)
        self.master.title('Note')
        self.master.geometry('250x250')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        frame = Frame(self)
        frame.pack()

        font_style = tk_font.Font(family="Helvetica", size=12)
        self.note_content = Text(frame, bg='#FFFF99', font=font_style)
        self.note_content.pack()

        self.m.add_command(label="New Note", command=self.new_note)
        self.m.add_command(label="Save", command=self.save_note)
        self.m.add_command(label="Change Title", command=self.change_title)
        self.m.add_separator()
        self.m.add_command(label="Delete", command=self.del_note)

        self.note_content.bind("<Button-3>", self.popup_menu)

    def popup_menu(self, event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()

    def new_note(self):
        create_new = Note(Toplevel(self))
        create_new.mainloop()

    def save_note(self):
        files = [('All Files', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
        file = asksaveasfile(mode='w', filetypes=files, defaultextension=files)
        contents = self.note_content.get(1.0, END)

        if file:
            file.write(contents)
            file.close()

    def change_title(self):
        self.new_window = Toplevel(self)
        self.new_window.title('Change Title')
        self.new_window.geometry("215x30")
        label = Label(self.new_window, text="Name of Title:")
        label.grid(row=0, column=0, sticky=W, pady=2)
        self.entry = Entry(self.new_window)
        self.entry.grid(row=0, column=1, pady=2)

        self.entry.bind('<Return>', self.finish_change)

    def finish_change(self, event):
        try:
            self.master.title(self.entry.get())
        finally:
            self.new_window.destroy()

    def del_note(self):
        self.master.destroy()

if __name__ == '__main__':
    root = Tk()
    note = Note(master=root)
    note.mainloop()
    root.destroy()
