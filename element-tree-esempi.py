from inspect import isfunction
from multiprocessing.spawn import import_main_path
import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Qui il Tutorial: https://www.youtube.com/watch?v=j0xr0-IAqyk

urlXml = 'https://www.frlt.camcom.it/bandi/rss.xml'
fileXml='sample.xml'

# display elementi di root
tree=ET.parse(fileXml)
root=tree.getroot().attrib
print(root)

for child in root.items():
    if child.tag == 'title':
        print(child[child], child.text.strip())

# printing the attributes of the
# first tag from the parent
# print(root[0].tag)



