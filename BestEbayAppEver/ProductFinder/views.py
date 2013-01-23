from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
import SearchForm
import DoRequest
import XmlParser
import ConfigReader


@csrf_exempt
def search(request):
    if request.method == 'POST':  # If the form has been submitted...
        product = str(request.POST['product'])  # look for variable product in POST
        results = DoRequest.findByKeyword(product)  # get the results for the search
        items = XmlParser.processMessage(results)
        return render_to_response('searchResults.html', {'items': items, 'searchTerm': product})
    else:
        return render_to_response('home.html')

def home(request):
    form = SearchForm
    return render_to_response('home.html', {
        'form': form,
    })

def configs(request):
    url = ConfigReader.getConfig('URL')
    default_url = ConfigReader.getConfig('DefaultURL')
    return render_to_response('configs.html', {'url': url, 'default_url': default_url})

def modifyConfigs(request):
    if request.method == 'POST':
        new_url = str(request.POST['url'])
        ConfigReader.setConfig('URL', new_url)
    return render('home.html')
