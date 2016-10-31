from django import forms

class CreateSearchForm(forms.Form):
	location = forms.CharField(label='Location', max_length=100,required=False)
	search = forms.CharField(label='search', max_length=100,required=False)