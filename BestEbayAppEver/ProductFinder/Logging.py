import xml.dom.minidom


def xmlResponse(message):
    msg = xml.dom.minidom.parseString(message)
    pretty_xml = msg.toprettyxml()
    log = open("response.xml", 'w')
    log.write(pretty_xml)
    log.close()
