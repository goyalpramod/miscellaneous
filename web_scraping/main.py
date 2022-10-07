#step 0 get the needed libraries, namely. html5lib,requests and bs4
from cgitb import html
from django.test import tag
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"
# step 1 Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# step 2 Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
# title = soup.title
# print(title)
# step 3 HTML tree traversal
#  Commonly used type of objects 
# 1. tag
# 2. Navigable string 
# 3. BeautifulSoup Object
#  4. Comment 

#  Get all paragraphs 
paras = soup.find_all('p')
# print(paras)

#  Get all anchor tags
anchors = soup.find_all('a')
# print(anchors)

all_links = set()

# get all links 
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

# get all the elements with a specific class 
# print(soup.find_all("p", class_="lead"))

# get the text form the tags
# print(soup.find('p').get_text())