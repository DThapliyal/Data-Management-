from django import forms
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
class StudentRegisteration(forms.ModelForm):
    class Meta:
        model=Users
        fields=['Name','Email','City','Department','Password']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'Email':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'City':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'Department':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'Password':forms.PasswordInput(render_value=True,attrs={'class':'form-control fw-bolder'}),
        }
class Sign_up(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control fw-bolder'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control fw-bolder'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'first_name':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'last_name':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
            'email':forms.TextInput(attrs={'class':'form-control fw-bolder'}),
        }

class userlogin(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=forms.CharField(label=_("Password"), strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))