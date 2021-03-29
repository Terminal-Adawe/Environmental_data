from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class indexloginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class registerForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget= forms.TextInput(attrs={'class':'form-control',}))
    email = forms.CharField(label='Email', max_length=100, widget= forms.EmailInput(attrs={'class':'form-control',}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control',}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',}))
    first_name = forms.CharField(label='First Name', max_length=100, widget= forms.TextInput(attrs={'class':'form-control',}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget= forms.TextInput(attrs={'class':'form-control',}))
    # is_staff = forms.BooleanField(required=False)