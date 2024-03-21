#! python3

from bs4 import BeautifulSoup
import requests
import os, sys

url = "https://xkcd.com"
src = "https://xkcd.com"
os.makedirs("./xkcd_images", exist_ok=True)

while not src.endswith("#"):
    try:
        res = requests.get(src)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        try:
            chunk = soup.find("div", id="comic")
            img_src = url + chunk.img["src"]
            img_title = chunk.img["src"].replace("//imgs.xkcd.com/comics/", "")

            print(f"name = {img_title} \nsource = {img_src}")

            if os.path.exists(os.path.join("xkcd_images", img_title)):
                print(f"image already exists, moving on to the next one.\n")

            else:
                r = requests.get(img_src)
                try:
                    with open(os.path.join("xkcd_images", img_title), "wb") as f:
                        f.write(r.content)
                        print(
                            f"image downloaded at {os.path.join('xkcd_images', img_title)}\n"
                        )
                except Exception as e:
                    print(f"Couldn't write content, {e} occured\n")

        except Exception as e:
            print(f"{e} occured, moving on to the next one")

        src = url + soup.find("a", rel="prev")["href"]

    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, cleaning up..")
        sys.exit(1)
