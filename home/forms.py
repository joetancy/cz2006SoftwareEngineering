from django import forms

class CreateSearchForm(forms.Form):
	location = forms.CharField(label='Location', max_length=100,required=False)