import pdb
import requests
from bs4 import BeautifulSoup
import re
import csv


with open('popular.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Name', 'Author',
                         'Desc', 'Rating', 'Rating Count', 'Install Count', 'Tested', 'Link'])

    sess = requests.Session()

    for i in range(1, 50):
        resp = sess.get(
            "https://wordpress.org/plugins/browse/popular/page/%d" % i)
        soup = BeautifulSoup(resp.text, 'html.parser')
        for item in soup.find_all('article'):
            link = item.find('h3').find('a').attrs['href']
            name = item.find('h3').find('a').text
            rating = len(item.find_all(class_='dashicons-star-filled')) + \
                len(item.find_all(class_='dashicons-star-half'))*0.5
            rating_count = int(item.find(
                class_='rating-count').text.split(' ')[0][1:].replace(',', ''))
            install_count = item.find(
                class_='active-installs').text.strip()
            install_count = int(re.findall(
                r'[\d,]+',  install_count)[0].replace(',', ''))
            author = item.find(
                class_='plugin-author').text.strip()
            desc = item.find(
                class_='entry-excerpt').text.strip()
            tested = item.find(
                class_='tested-with').text.strip() if item.find(class_='tested-with') else ''

            print(name, author, desc, rating, rating_count,
                  install_count, tested, link)
            spamwriter.writerow([name.encode('utf-8'), author.encode('utf-8'), desc.encode('utf-8'),
                                 str(rating), str(rating_count), str(install_count), tested, link])
