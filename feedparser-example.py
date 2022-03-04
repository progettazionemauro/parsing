# feedpareser si trova qui: https://feedparser.readthedocs.io/en/latest/common-rss-elements.html
import feedparser

# 4 marzo 2022 dopo ore di sacrificio e sudore mentale finalmente
# sono riuscito a trovare la soluzione per importare 
# il tag description rendendolo "pulito" questa è la 
# funzione che si trova qui https://pypi.org/project/html2text/
import html2text
urlXml = 'https://www.frlt.camcom.it/bandi/rss.xml'
d = feedparser.parse(urlXml, sanitize_html=True)


titolo=d.entries[0].title

descrizione=d.entries[1].description


descrizione_pulita = html2text.html2text(descrizione)


verificaTipo=d.entries[0].summary_detail.type

root=d['feed']
detail=d['feed']['title_detail']
link=d['feed']['link']



print(titolo)
print(20*"----")

print(descrizione_pulita)
print(20*"****")

print(link)
print(20*"//")

print(verificaTipo)
print(20*"OOO")

""" print(root)
print(20*"((()))")
print(detail)
print(20*"****") """