from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import GITHUB_USER, GITHUB_PASS
import time
import sys

# Initialize chrome webdriver
driver = webdriver.Chrome()

driver.get('https://github.com/login')
# Login field is id='login_field' & password field is 'password'
username = driver.find_element_by_id('login_field')
password = driver.find_element_by_id('password')

# Key in <input> fields
username.send_keys(GITHUB_USER)
time.sleep(1)
password.send_keys(GITHUB_PASS)
time.sleep(1)

# Automate click on login button
press_login = driver.find_element_by_xpath("//input[@value='Sign in']")
time.sleep(1)
press_login.click()
time.sleep(1)

# Specify any name you want to be honest
name_list = ['john', 'tom', 'jump']

# Search for users
# Search via best match url='https://github.com/search?o={}&q=user&s=&type={}'
# We want to use type=Users you can use other types as well

for name in name_list:
    for page in range(1, 100):
        url = 'https://github.com/search?p={}&q={}&type=Users'.format(
            page, name)
        driver.get(url)
        time.sleep(1)

        # Find and press follow button
        follow_user = driver.find_elements_by_xpath(
            "//input[@aria-label='Follow this person']")

        try:
            for i in follow_user:
                i.submit()
        except:
            pass
        time.sleep(1)

driver.close()
