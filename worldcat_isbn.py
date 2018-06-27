#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
import requests
# http://www.worldcat.org/webservices/catalog/content/libraries/isbn/9788360940068?wskey=a1vkxyTxLTHhknwO9VXF9BNiI8bZ6R9BzzHMTR0Qn4XZ67BLSQuTEmGyIa4wGnqE07TexyzGjlsPQYxd&limit=1000

def parse_xml(xml):

    libraries = []
    outcome = 1
    xml = xml.replace("\n", "")
    tree = ET.fromstring(xml)
    holdings = tree.findall("holding")
    for holding in holdings:
        location = holding.find("physicalLocation")
        library = location.text
        libraries.append(library)
    return libraries

def main():

#    isbn = sys.stdin
    isbn = "9788360940068"
    url = "http://www.worldcat.org/webservices/catalog/content/libraries/isbn/{isbn}"
    wskey = [insert apikey]
    limit = "1000"
    url = url.replace("{isbn}", isbn)
    payload = {"wskey": wskey, "limit": limit}
    r = requests.get(url, params=payload)
    xml = r.content
    response = parse_xml(xml)
    print isbn + "	" + str(response)

if __name__=="__main__":
    sys.exit(main())
