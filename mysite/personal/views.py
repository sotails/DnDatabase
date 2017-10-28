from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

from .models import your_name
# Create your views here.
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	
            # process the data in form.cleaned_data as required
           
            name = form.cleaned_data['your_name']
            obj = your_name(name)
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'personal/yourname.html', {'form': form})

def index(request):
	return render(request, 'personal/home.html')

	
def form(request):
	return render(request, 'personal/form.html')
