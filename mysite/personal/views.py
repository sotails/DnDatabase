from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User

from .models import *
from django.http import JsonResponse
from django.db import IntegrityError
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
			item_type1 ="item"
			type = itform.cleaned_data['item_type']
			print(type)
			if type == "1":
				item_type1 = "Item"
			elif type == "2":
				item_type1 = "Spell"
			else:
				item_type1 = "Weapon"
			item_name2 = itform.cleaned_data['item_name']
			item_description3 =itform.cleaned_data['item_description']
			obj = item(item_type=item_type1,item_name=item_name2,item_description=item_description3)
			obj.save()


	else:
		itform = ItemForm()


	return render(request, 'personal/form.html',{'form': itform ,'hello':hello})


def Uform(request):
	if request.method == 'POST':
		Uf = UserForm(request.POST)
		if Uf.is_valid():
			try:
				user = User.objects.create_user(Uf.cleaned_data['first_name'],Uf.cleaned_data['password'],Uf.cleaned_data['email'])
				user.last_name =Uf.cleaned_data['last_name']
				user.save()
			except IntegrityError:
				return render(request, 'personal/UForm.html',{'form': Uf})



	else:
		Uf = UserForm()
		return render(request, 'personal/UForm.html',{'form': Uf})
	return render(request, 'personal/home.html')


#def simple_list(request):
	#queryset = Simple.objects.all()
	#table = SimpleTable(queryset)
#	return render(request, 'simple_list.html', {'table':table})
