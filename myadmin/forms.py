from django import forms
from .models import videoDetails


class videoDetailsForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title','size': '48','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'description','style': 'height: 120px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	
	class Meta:

		model=videoDetails
		fields=['title', 'description','video_file','thumbnail']





