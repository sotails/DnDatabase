from django import forms

class ItemForm(forms.Form):
	item_type = forms.CharField(label='option', max_length=100)
	item_name = forms.CharField(label='name', max_length=200)
	item_description = forms.CharField(label='description',min_length=1)


  