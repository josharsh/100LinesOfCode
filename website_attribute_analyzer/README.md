## WEBSITE ATTRIBUTE SCRAPPER
- - -
This is a python script that allows you to extract and analyze specific attributes in a website.
### Walkthrough of the program
* The program asks you for a website URL
* The program asks you to enter the attribute you want to retrieve from the website (such as `<title>`, `<a>`, `<img>`, class or id)
* If your input is a normal html tag such as `<button>` `<div>` or `<p>`, the program returns a list of all the content inside the webpage
* If your input is a class or id, when the second prompt is asked (which attribute do you want to check), type in the text `id` or `class` accordingly which will return all the existing classes/ids in a website. Further, it will ask you to name or mention the number of the class/id. When you do, the program will return a list of all the content within the class/id
  * PS: I personally use this feature the most.
* If your input is an anchor tag `<a>` it will return all the links ie..,`href` in the webpage.
* If your input is an image tag `<img>` it will return all the sources ie..,`src` in the webpage.

### Language Used
Python 3.11

### Requirements
If the program doesn't work, make sure to install these-
* Python 3
  * [Install python 3](https://www.python.org/downloads/)
* pip
  * [Install pip](https://pip.pypa.io/en/stable/installation/)
* requests - python package
  * ``pip install requests``
* BeautifulSoup
  * ``pip install bs4``
 
  Author: Sai Dhanush V
