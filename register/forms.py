from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, required=True)
    first_name = forms.CharField(
        label='First Name', max_length=20, required=True)
    last_name = forms.CharField(
        label='Last Name', max_length=20, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
        label='Password', max_length=40, widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(
        label='Confirm Password', max_length=40, widget=forms.PasswordInput(), required=True)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, required=True)
    password = forms.CharField(
        label='Password', max_length=40, widget=forms.PasswordInput(), required=True)
