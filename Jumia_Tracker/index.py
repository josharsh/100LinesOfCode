#scrap jumia website
import requests
from bs4 import BeautifulSoup
import json

#function to get the product details
def get_product_details(product_link):
    #get the product page
    data = {}
    all_data = []
    product_page = requests.get(product_link)
    product_soup = BeautifulSoup(product_page.content, 'html.parser')
    articles = product_soup.find_all('article', class_='prd')
    for article in articles:
        name = article.find('div', class_='name')
        if not name:
            name = article.find('h3', class_='name')
            
        if name:
            name = name.text.strip()
        
        price = article.find('div', class_='prc')
        if price:
            price = price.text.strip()
        
        data = {
            'name': name,
            'price': price,
        }
        print(data)
        
        all_data.append(data)
    return all_data

    

#write the product details to a json file
def write_to_json(product_details):
    with open('jumia.json', 'w') as file:
        json.dump(product_details, file, indent=4)

#function to get the page links
def get_page_links():
    #get the page
    url = input('Enter the jumia url of the page you want to scrape(select a url of a main category): ')
    products = get_product_details(url)
    write_to_json(products)
    print('Done')


if __name__ == '__main__':
    # scrape_product_details
    get_page_links()