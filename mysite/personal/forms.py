
from django import forms

class ItemForm(forms.Form):
	item_type = forms.ChoiceField(choices=[('1','Item'),('2','Spell') ,('3','Weapon')])
	item_name = forms.CharField(label='name', max_length=200)
	item_description = forms.CharField(label='description',min_length=1)

class UserForm(forms.Form):
	first_name = forms.CharField(label='Firstname', max_length=200)
	last_name = forms.CharField(label='Lastname', max_length=200)
	email = forms.CharField(label='Email', max_length=200)
	password = forms.CharField(label='Password', max_length=200)
