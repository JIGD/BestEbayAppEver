import ConfigReader

# specify eBay API dev,app,cert IDs
devID = ConfigReader.getConfig("Developer")
appID = ConfigReader.getConfig("Application")
certID = ConfigReader.getConfig("Certificate")

#get the server details from the config file

serverDirectory = ConfigReader.getConfig("Directory")


def buildHttpHeaders():
    httpHeaders = {'X-EBAY-SOA-OPERATION-NAME': 'findItemsByKeywords',\
                   'X-EBAY-SOA-SERVICE-VERSION': '1.3.0',
                   'X-EBAY-SOA-REQUEST-DATA-FORMAT': 'XML',
                   'X-EBAY-SOA-GLOBAL-ID': 'EBAY-US',
                   'X-EBAY-SOA-SECURITY-APPNAME': appID,
                   'Content-Type': 'text/xml;charset=utf-8'}
    return httpHeaders


def buildRequestXml(keyword):
    requestXml = "<?xml version='1.0' encoding='utf-8'?>" + \
              "<findItemsByKeywordsRequest " + \
              "xmlns=\"http://www.ebay.com/marketplace/search/v1/services\">" +\
              "<keywords>" + keyword + "</keywords>" + \
              "<paginationInput>" + \
              "<entriesPerPage>5</entriesPerPage>" + \
              "</paginationInput>" + \
              "</findItemsByKeywordsRequest>"
    return requestXml


def getServerURL():
    serverURL = ConfigReader.getConfig("URL")
    return serverURL
