"""module for fetching the daily bible verse from ourmanna.com"""

import tkinter as tk
import requests

URL = "https://beta.ourmanna.com/api/v1/get?format=json&order=daily"

HEADERS = {"accept": "application/json"}

root = tk.Tk()
root.title("Daily Bible Verse")


class DailyBibleVerse:
    """class for fetching the daily bible verse from ourmanna.com"""
    def __init__(self, gui_ref=None):
        self.gui_ref = gui_ref
        self.response = None
        self.text = None
        self.reference = None
        self.version = None

        try:
            resp = requests.get(URL, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            self.response = resp
            data = resp.json()
            details = data.get("verse", {}).get("details", {})
            self.text = details.get("text")
            self.reference = details.get("reference")
            self.version = details.get("version")
            print(f"{self.text} - {self.reference} ({self.version})")
        except requests.RequestException as exc:
            print(f"Warning: failed to fetch initial verse: {exc}")

    def daily_bible_verse(self):
        """Fetch and return the daily bible verse as a string.

        This performs a fresh request so the GUI button returns an updated verse.
        """
        print("Fetching daily verse...")

        try:
            resp = requests.get(URL, headers=HEADERS, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            details = data["verse"]["details"]
            self.text = details["text"]
            self.reference = details["reference"]
            self.version = details["version"]
            result = f"{self.text} - {self.reference} ({self.version})"
        except requests.RequestException as exc:
            result = f"Error fetching verse: {exc}"

        if self.gui_ref is not None:
            self.gui_ref.verse_var.set(result)

        return result

class GUI:
    """class for the GUI"""
    def __init__(self, root_ref):
        self.verse_var = tk.StringVar(master=root_ref, value="Fetching daily verse...")
        self.verse_label = tk.Label(root_ref, textvariable=self.verse_var, font=("Arial", 12))
        self.verse_label.pack(pady=10)

if __name__ == "__main__":
    gui = GUI(root)
    daily_verse = DailyBibleVerse(gui)

    get_verse_button = tk.Button(root, text="Get Daily Verse",
                                font=("Arial", 12), command=daily_verse.daily_bible_verse)
    get_verse_button.pack(pady=10)
    daily_verse.daily_bible_verse()
    root.mainloop()
