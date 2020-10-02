import pdb
import requests
from bs4 import BeautifulSoup
import re
import csv
import os


sess = requests.Session()

URLS = [
"https://wordpress.org/plugins/contact-form-7/",
]

for url in URLS:
    resp = sess.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # pdb.set_trace()
    link = soup.find_all(class_="plugin-download")[0].attrs["href"]
    filename = link.split("/")[-1]
    print(link)
    os.system("axel -a -n 16 %s && unzip %s" % (link, filename))
