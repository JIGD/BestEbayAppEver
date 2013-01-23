from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
import SearchForm
import DoRequest


@csrf_exempt
def search(request):
    if request.method == 'POST':  # If the form has been submitted...
        product = str(request.POST['product'])  # look for variable product in POST
        DoRequest.findByKeyword(product)
        return render_to_response('searchResults.html', {'output': product}) 
    else:
        return render(request, 'home.html')


def home(request):
    form = SearchForm
    return render_to_response('home.html', {
        'form': form,
    })


def searchResults(request, results):
    return render('searchResults.html', results)
