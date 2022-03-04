from inspect import isfunction
from multiprocessing.spawn import import_main_path
import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

urlXml = 'https://www.frlt.camcom.it/bandi/rss.xml'
fileXml='sample.xml'

tree=ET.parse(fileXml)
root=tree.getroot()

# Display classes
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)
        print (20*"¬¬¬")

# Display functions in ET Module
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)