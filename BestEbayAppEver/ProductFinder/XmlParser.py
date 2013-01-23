import xml.etree.ElementTree as ET


def processMessage(message):
    wtfprefix = "{http://www.ebay.com/marketplace/search/v1/services}"
    results = ET.fromstring(message)  # convert to XML
    items = results.find(wtfprefix + 'searchResult')
    items = items.findall(wtfprefix + 'item')
    total_items = []
    for child in items:
        item = {}  # clean the item dictionary
        for children in child:
            item[children.tag[52:]] = children.text  # remove nasty prefix and store each value with its tag as a key on an item
        total_items.append(item)  # inser item into the list
    return total_items
