
from django import forms

class ItemForm(forms.Form):
	item_type = forms.ChoiceField(choices=[('1','Item'),('2','Spell') ,('3','Weapon')])
	item_name = forms.CharField(label='name', max_length=200)
	item_description = forms.CharField(label='description',min_length=1)

class UserForm(forms.Form):
	username = forms.CharField(label='uname', max_length=200)
	password = forms.CharField(label='password', max_length=200)
	email = forms.CharField(label='email', max_length=200)
	first_name = forms.CharField(label='fname', max_length=200)
	last_name = forms.CharField(label='lname', max_length=200)
