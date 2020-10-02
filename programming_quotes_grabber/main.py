import requests

def getQuote():
    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    resp = requests.get(url)
    if resp.status_code != 200:
        error('request to server could not be made')

    data = resp.json()
    return data

if __name__ == '__main__':
    data = getQuote()
    print('😃 ' + data['quote'])
    print('by ' + data['author'] + ' 😃')
