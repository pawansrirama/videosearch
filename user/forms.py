from django import forms
from .models import registerDetials

GENDER_CHOICES=[
 ('Male', 'Male'),
 ('Female', 'Female'),
 ('Others','Others'),
]


class registerDetialsForm(forms.ModelForm):
	gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
	firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name','size': '25','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name','size': '25','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	birthdayDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','size': '30','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	phoneNumber = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number','size': '25','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	emailAddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email','size': '25','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password','size': '25','style': 'height: 45px; border: 2px solid lightgrey; border-radius: 5px; box-sizing: border-box;'}))
	class Meta:

		model=registerDetials
		fields=['firstName','lastName','birthdayDate','gender','emailAddress','phoneNumber','password']