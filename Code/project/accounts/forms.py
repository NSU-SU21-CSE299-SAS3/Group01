from django import forms
from .models import Account

# creating forms
class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Enter Password',
		}))

	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder': 'Confirm Password',
		}))

	class Meta:
		model = Account
		fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']