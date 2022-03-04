import xml.dom.minidom

with open('sample.xml') as xmldata:
    xml = xml.dom.minidom.parseString(xmldata.read())  # or xml.dom.minidom.parseString(xml_string)
    xml_pretty_str = xml.toprettyxml()

print (xml_pretty_str)

