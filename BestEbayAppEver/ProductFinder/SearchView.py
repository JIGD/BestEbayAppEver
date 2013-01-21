from django.shortcuts import render
from django.http import HttpResponseRedirect

def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/searchResult/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'home.html', {
        'form': form,
    })