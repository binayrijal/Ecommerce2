from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation


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
        'class':'form-control',
    }))

class MypasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("old password"),strip=False, widget=forms.PasswordInput(attrs={
        'autofocus':True,
        'autocomplete':'current-password',
        'class': 'form-control',
    }))
    new_password1=forms.CharField(label=_("new password"),strip=False,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'autocomplete':'new-password',

    }),help_text=password_validation.
    password_validators_help_text_html()
    )

    new_password2=forms.CharField(label=_("repeat password"),strip=False,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'autocomplete':'new-password',

    }))