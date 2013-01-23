import requests
import BuildRequest
import Logging


url = BuildRequest.getServerURL()


def findByKeyword(keyword):
    xml_request = BuildRequest.buildRequestXml(keyword)
    headers = BuildRequest.buildHttpHeaders()
    r = requests.post(url, data=xml_request, headers=headers)
    response = r.text
    Logging.xmlResponse(response)
    return response
