from urllib import response
import requests
import urllib.request
import re
from bs4 import BeautifulSoup


# legge il contenuto HTML
urlHtml = 'https://en.wikipedia.org/wiki/Main_Page'
response=requests.get(urlHtml)



# trova il contenuto html
htmlSoup=BeautifulSoup(response.text, 'html.parser')

# trova il tag
#xml_tag=BeautifulSoup.find('item')

for tag in htmlSoup('a'):
    print(tag.get('href'))
    print (20*"###")

for tag_1 in htmlSoup.find_all(re.compile("^b")):
    print(tag_1)


