#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
import requests

# example api url:
# https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/99939650000541?view=full&expand=None&apikey=l7xx2af7939c63424511946e0fcdc35fe22a

def parse_marcxml(marcxml):

    ######################################################################
    # docs: https://docs.python.org/2/library/xml.etree.elementtree.html #
    ######################################################################
    # xml snippet:
    #  <datafield ind1="1" ind2="0" tag="245">
    #    <subfield code="a">War and peace /</subfield>
    #    <subfield code="c">Leo Tolstoy.</subfield>
    #  </datafield>
    tree = ET.fromstring(marcxml)
    record = tree.find('record')
    datafields = record.findall('datafield')
    for df in datafields:
        tag = df.get('tag')
        if tag == '245':
            subfields = df.findall('subfield')
            for sf in subfields:
                code = sf.get('code')
                if code == 'a':
                    title = sf.text
                elif code == 'c':
                    author = sf.text
    return(title + " " + author)

def main():

    #############
    # variables #
    #############
    url = "https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/{mmsid}"
    apikey = "l7xx2af7939c63424511946e0fcdc35fe22a"
    mmsid = "99939650000541"
    view = "full"
    expand = "null"
    ################
    # api call GET #
    ################
    payload = {'apikey': apikey, 'view': view, 'expand': expand}
    url = url.replace('{mmsid}', mmsid)
    r = requests.get(url, params = payload)
    ##################
    # process result #
    ##################
    ### uncomment to see marcxml
    #print(r.content)
    marcxml = r.content
    result = parse_marcxml(marcxml)
    print(result)

if __name__=="__main__":
    sys.exit(main())
