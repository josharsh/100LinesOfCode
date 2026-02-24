"""This script downloads all the comics from xkcd.com
and saves them in a folder named 'xkcd_images'.
The script uses the BeautifulSoup library to parse the HTML content of the xkcd website and 
extract the image URLs. 
It then uses the requests library to download the images and save them to the local filesystem.
The script also handles exceptions that may occur during the download process,
such as network errors or file writing errors, and prints appropriate messages to the console. 
The script continues to download comics until it reaches the end of the comic list,
which is indicated by a "#" in the URL.
To run the script, make sure you have the BeautifulSoup and requests libraries installed,
and then execute the script in a Python environment.
The downloaded images will be saved in the "xkcd_images"
folder in the same directory as the script."""

#!python3

import os
import sys
from bs4 import BeautifulSoup
import requests

URL= "https://xkcd.com"
SRC= "https://xkcd.com"
os.makedirs("./xkcd_images", exist_ok=True)

while not SRC.endswith("#"):
    try:
        res = requests.get(url=SRC, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        try:
            chunk = soup.find("div", id="comic")
            img_src = URL + chunk.img["src"]
            img_title = chunk.img["src"].replace("//imgs.xkcd.com/comics/", "")

            print(f"name = {img_title} \nsource = {img_src}")

            if os.path.exists(os.path.join("xkcd_images", img_title)):
                print("image already exists, moving on to the next one.\n")

            else:
                r = requests.get(img_src, timeout=10)
                try:
                    with open(os.path.join("xkcd_images", img_title), "wb") as f:
                        f.write(r.content)
                        print(
                            f"image downloaded at {os.path.join('xkcd_images', img_title)}\n"
                        )
                except OSError as e:
                    print(f"Couldn't write content, {e} occured\n")

        except (requests.RequestException, KeyError) as e:
            print(f"{e} occured, moving on to the next one")

        SRC= URL + soup.find("a", rel="prev")["href"]

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, cleaning up..")
        sys.exit(1)
