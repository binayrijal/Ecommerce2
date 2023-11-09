from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _



class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'enter your username here',
    }))

    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
         'placeholder':'enter your email here',
    }))

    password1=forms.CharField(label='password1',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'enter your password here',
        

    }))
    password2=forms.CharField(label='confirm password(again)',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
         'placeholder':'enter your password here',
    }))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={'emai':'Email'}


class UserLoginForm(AuthenticationForm):

    username=UsernameField(widget=forms.TextInput(attrs={
        'autofocus':True,
        'class':'form-control',
       
    
    }))

    password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password',
        'class':'form-control'
    }))