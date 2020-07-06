# Given a species name, this script returns the IUCN category/status of the species
from bs4 import BeautifulSoup
import requests

def get_soup():
    species_name = input('Enter the name of the species: ')
    result = requests.get(f'https://en.wikipedia.org/wiki/{species_name}')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    return soup

def get_status():
    soup = get_soup()
    try:
        species_name = soup.select_one('.mw-redirect[href="/wiki/Least_Concern"]').text
    except AttributeError:
        try:
            species_name = soup.select_one('a[href="/wiki/Vulnerable_species"]').text
        except  AttributeError:
            try:
                species_name = soup.select_one('.mw-redirect[href="/wiki/Near_Threatened"]').text
            except  AttributeError:
                try:
                    species_name = soup.select_one('a[href="/wiki/Endangered_species"]').text
                except  AttributeError:
                    try:
                        species_name = soup.select_one('.mw-redirect[href="/wiki/Critically_endangered_species"]').text
                    except  AttributeError:
                        try:
                            species_name = soup.select_one('.mw-redirect[href="/wiki/Extinct_in_the_Wild"]').text
                        except  AttributeError:
                            try:
                                species_name = soup.select_one('a[href="/wiki/Extinction"]').text
                            except  AttributeError:
                                species_name = 'Could not find status... Check spelling or perhaps try the scientific name'
    return species_name
print(f'Status:\n> {get_status()}')