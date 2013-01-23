import requests
import BuildRequest
import Logging


url = BuildRequest.getServerURL()


def findByKeyword(keyword):
    xml_request = BuildRequest.buildRequestXml(keyword)
    headers = BuildRequest.buildHttpHeaders()
    r = requests.post(url, data=xml_request, headers=headers)
    Logging.xmlResponse(r.text)


findByKeyword("Harry potter")
