# Welcome Commander...
from django import forms
from .models import *

class SketchModel(forms.ModelForm):
	class Meta:
		model = Sketch
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'titleId', 'placeholder': 'A Sweet Name'}),
			
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'id': 'descriptionId', 'class' : 'form-control', 'placeholder': 'About This Images'}),
		
		}
		
class NatureModel(forms.ModelForm):
	class Meta:
		model = Nature
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'titleId', 'placeholder': 'A Sweet Name'}),
			
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'id': 'descriptionId', 'class' : 'form-control', 'placeholder': 'About This Images'}),
		
		}
		
class PortraitModel(forms.ModelForm):
	class Meta:
		model = Portrait 
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'titleId', 'placeholder': 'A Sweet Name'}),
			
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'id': 'descriptionId', 'class' : 'form-control', 'placeholder': 'About This Images'}),
		
		}
		
class CarsModel(forms.ModelForm):
	class Meta:
		model = Cars 
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'titleId', 'placeholder': 'A Sweet Name'}),
			
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'id': 'descriptionId', 'class' : 'form-control', 'placeholder': 'About This Images'}),
		
		}
		
class WildlifeModel(forms.ModelForm):
	class Meta:
		model = Wildlife 
		fields = '__all__'
		widgets = {
			'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id': 'titleId', 'placeholder': 'A Sweet Name'}),
			
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 3, 'id': 'descriptionId', 'class' : 'form-control', 'placeholder': 'About This Images'}),
		
		}
