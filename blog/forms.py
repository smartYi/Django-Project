from django import forms

from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'content'
		]

	def clean(self):
		cleaned_data = super(PostForm, self).clean()

		return cleaned_data




class RegistrationForm(forms.Form):
	username = forms.CharField(max_length = 30)
	first_name = forms.CharField(label='First Name',
					widget = forms.TextInput())
	last_name = forms.CharField(label = 'Last Name',
					widget = forms.TextInput())
	password1 = forms.CharField(max_length = 200,
				   label='Password', 
				   widget = forms.PasswordInput())

	password2 = forms.CharField(max_length = 200,
				   label='Confirm password',
				   widget = forms.PasswordInput())

	

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		password1 = cleaned_data.get('password1')
		password2 = cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords did not match.")

		return cleaned_data

	

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username__exact=username):
			raise forms.ValidationError("Username is already taken.")
		return username



		