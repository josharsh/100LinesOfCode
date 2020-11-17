import requests

url = "http://checkip.dyndns.org"
request = requests.get(url)
clean = request.text.split(': ', 1)[1]
your_ip = clean.split('</body></html>', 1)[0]

print (your_ip)
