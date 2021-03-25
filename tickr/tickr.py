import tkinter as tk
import requests
from bs4 import BeautifulSoup
import time

# Tickr v1 by Droogy
# This programs grabs the headlines for articles from the New York Times homepage
# and parses these results in a news-style ticker you would typically see

 
class Marquee(tk.Canvas):
    #adjust fps for speed
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=60):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
        self.fps = fps
 
        # render the text off screen first, then asking the canvas
        # how much space is needed 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        
        # width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=500, height=height)
        
        # start animation
        self.animate()
 
    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)
 
        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)

root = tk.Tk()
# this will hold the headlines
text = []
url = 'https://www.nytimes.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')

# heres where the magic happens, beautiful soup searches for all header tags
# and strips the text for us
# need to add regex here because we're grabbing some garbage headlines
# and NYT seems to have annoying class names for some headlines to filter thru
for heading in soup.find_all(['h1', 'h2', 'h3']):
    header=heading.text.strip()
    text.append(header)

#add padding so the headlines aren't right next to each other and spaced out    
padding = ' ' * 60

# using this list comprehension we pre-pend 60 empty spaces to each headline 
padded_text=[padding + x for x in text]
# if running into problems, start debugging text list before and after padded_text 
# and make sure values are there and formatted to our liking
# print(text)
while True:
    # text in Marquee is declared to be every value in padded_text with a neat trick
    marquee = Marquee(root, text=[x for x in padded_text], borderwidth=1, relief="sunken")
    marquee.pack(side="top", fill="x", pady=20)
    root.mainloop()
