from django import forms 
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Postfrom(forms.ModelForm):
    class Meta:
        model=Post
        fields=["text","photo"]


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model =User
        fields=('username','email','password1','password2')#yha par tuple use hoga kyuki builtin h jo hum bnaye usme array use hoga upr wale ki trh
