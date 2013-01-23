import xml.dom.minidom


def xmlResponse(message):
    msg = xml.dom.minidom.parseString(message)
    pretty_xml = msg.toprettyxml()
    log = open("response.txt", 'w')
    log.write(pretty_xml)
    log.close()
