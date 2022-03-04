from urllib import response
from flask import request
import requests
import urllib.request
import re
from bs4 import BeautifulSoup, SoupStrainer

#
# legge in contenuto XML

#urlXml = 'https://www.frlt.camcom.it/bandi/rss.xml'
urlXml = 'https://www.w3schools.com/xml/note.xml'

req=urllib.request.urlopen(urlXml)


xml=requests.get(urlXml)


# trova il contentuto xml
xmlSoup = BeautifulSoup(xml, 'xml').prettify

# trova il tag


# Con questo loop riesco ad effettuare il parse su tutti gli items

""" for item in xmlSoup.findAll('description')[5:]:
    print(item.text)
    print (20*"###") """

contenuto=xmlSoup
soupContent=BeautifulSoup(contenuto, 'lxml')
print(contenuto)