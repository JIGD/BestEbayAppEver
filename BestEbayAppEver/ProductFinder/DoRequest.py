import requests
import BuildRequest
import Logging


def findByKeyword(keyword):
    url = BuildRequest.getServerURL()
    xml_request = BuildRequest.buildRequestXml(keyword)
    headers = BuildRequest.buildHttpHeaders()
    r = requests.post(url, data=xml_request, headers=headers)
    response = r.text
    Logging.xmlResponse(response)
    return response
