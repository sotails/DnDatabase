from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ItemForm

from .models import item
from django.http import JsonResponse
# Create your views here.

def index(request):
	return render(request, 'personal/home.html')


def form(request):
	#allObjects = item.objects.all()#.values('item_type','item_name','item_description')
	hello=(item.objects.all())
	hello= set(hello)

	if request.method == 'POST':
		itform = ItemForm(request.POST)
		if itform.is_valid():
			item_type1 = itform.cleaned_data['item_type']
			item_name2 = itform.cleaned_data['item_name']
			item_description3 =itform.cleaned_data['item_description']
			obj = item(item_type=item_type1,item_name=item_name2,item_description=item_description3)
			obj.save()


	else:
		itform = ItemForm()


	return render(request, 'personal/form.html',{'form': itform ,'hello':hello})
