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


	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['phone_number'].widget.attrs['placeholder'] = '+8801XX-XXXX-XXX'

		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'