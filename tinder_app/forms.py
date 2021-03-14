from django import forms
from . models import DogBreed, Dog


class DogForm(forms.ModelForm):
	class Meta:
		model = Dog
		fields = '__all__'
		widgets = {
			'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
		}