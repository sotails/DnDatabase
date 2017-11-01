from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm

from .models import item
# Create your views here.

def index(request):
	return render(request, 'personal/home.html')

	
def form(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			item_type1 = form.cleaned_data['item_type']
			item_name2 = form.cleaned_data['item_name']
			item_description3 =form.cleaned_data['item_description']
			obj = item(item_type=item_type1,item_name=item_name2,item_description=item_description3)
			obj.save()
			return HttpResponseRedirect('personal/home.html')
	else:
		form = ItemForm()

	return render(request, 'personal/form.html',{'form': form})
