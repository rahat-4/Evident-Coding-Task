from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import MyUser

class RegisterForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    #modifying form fields
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Full Name"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password Confirmation"}))
    
    class Meta:
        model = MyUser
        fields = ['full_name', 'email', 'password1', 'password2',]


class LoginForm(AuthenticationForm):
    """
    A form for login users using email and password.
    """
    #modifying form fields
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Email"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    class Meta:
        model = MyUser
        fields = ['username', 'password', ]