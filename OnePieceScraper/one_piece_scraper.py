#! python3

import sys, webbrowser, requests, re, math
from bs4 import BeautifulSoup
from tqdm import tqdm

def check_link(link):
	return link.endswith(('.mkv', '.avi'))

def sort_links(links):
	links = sorted(links, key= lambda x: int(re.search(r'\d+', x.text).group()))
	return links

if __name__ == '__main__':
		DN_STR = 'https://storage.kanzaki.ru/ANIME___/One_Piece/'
		itr=0
		BLOCK_SIZE = 1024
		html = requests.get(DN_STR)
		soup = BeautifulSoup(str(html.text), "html.parser")# lxml is just the parser for reading the html
		links = soup.find_all('a') # this is the line that does what you want
		links = links[2:]
		links = sort_links(links)
		for index in range(0, len(links)):
			if not check_link(links[index]['href']):
				continue
			print('Downloading Link : {}'.format(links[index].text))
			res = requests.get(DN_STR+links[index]['href'], stream = True)
			total_size = int(res.headers.get('content-length', 0))
			bytes_written = 0
			with open('./{}'.format(links[index].text), 'wb') as f_ep:
				for data in tqdm(res.iter_content(BLOCK_SIZE),
								 total = math.ceil(total_size / BLOCK_SIZE) ,
								 unit = 'KB',
								 unit_scale = True):
					bytes_written += f_ep.write(data)
