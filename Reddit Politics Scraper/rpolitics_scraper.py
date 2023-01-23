import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# The URL to be scraped: the top threads in the r/politics page
url = 'https://www.reddit.com/r/politics/top/'

# You must download a valid browser driver to use this program. Modify the path below to reflect
# the location of your chromedriver.exe file.
# Download here: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(executable_path=r'/Users/jongong/chromedriver.exe')
driver.get(url)

# Scrolling down for 20 seconds to render additional threads to scrape
driver.execute_script("window.scrollTo(0, 1000000)")
time.sleep(20)

# Obtaining the rendered page source from the artificial chrome browser
html = driver.page_source
driver.close()

soup = BeautifulSoup(html, 'html.parser')

# Creating the word_count dictionary to add to 
word_count = {}

# the h3 tag with the specified class is the container for each reddit thread title
for title in soup.find_all('h3', class_="_eYtD2XCVieq6emjKBH3m"):
    title_as_array = title.text.split(" ")
    for word in title_as_array:
        if word_count.get(word) == None:
            word_count[word] = 1
        else:
            word_count[word] += 1


# Converting the dictionary into a pandas dataframe for visual inspection
df = pd.DataFrame(word_count.items(), columns = ['Word', 'Count']).sort_values(by = 'Count', ascending = False).reset_index(drop = True)

df.to_csv('reddit_politics_word_count.csv')