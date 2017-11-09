
from django import forms

class ItemForm(forms.Form):
	item_type = forms.ChoiceField(choices=[('1','Item'),('2','Spell') ,('3','Weapon')])
	item_name = forms.CharField(label='name', max_length=200)
	item_description = forms.CharField(label='description',min_length=1)


  