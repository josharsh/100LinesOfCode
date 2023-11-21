import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

class DiaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Personal Diary")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.create_button = tk.Button(master, text="Create Entry", command=self.create_entry)
        self.create_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Entries", command=self.view_entries)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Diary", command=self.confirm_delete_diary)
        self.delete_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack(pady=5)

    def create_entry(self):
        entry_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_text = self.text_area.get("1.0", tk.END).strip()
        entry = f"\n{entry_date}\n{entry_text}\n"
        self.save_entry(entry)
        
        # Clear the text area after creating an entry
        self.text_area.delete("1.0", tk.END)

    def save_entry(self, entry, filename="diary.txt"):
        with open(filename, "a") as file:
            file.write(entry)
        print("Entry saved successfully.")

    def view_entries(self, filename="diary.txt"):
        try:
            with open(filename, "r") as file:
                entries = file.readlines()
                if not entries:
                    self.show_message("No entries found.")
                else:
                    entries_text = "----- Your Entries -----\n"
                    for entry in entries:
                        entries_text += entry.strip() + "\n"
                    entries_text += "------------------------"
                    self.show_message(entries_text)
        except FileNotFoundError:
            self.show_message("Diary file not found. No entries exist yet.")

    def show_message(self, message):
        message_window = tk.Toplevel(self.master)
        message_window.title("Entries")
        message_label = tk.Label(message_window, text=message, padx=10, pady=10)
        message_label.pack()

    def confirm_delete_diary(self):
        confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the entire diary?")
        if confirmation:
            self.delete_diary()

    def delete_diary(self, filename="diary.txt"):
        try:
            os.remove(filename)
            print("Diary deleted successfully.")
        except FileNotFoundError:
            print("Diary file not found. No entries to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
