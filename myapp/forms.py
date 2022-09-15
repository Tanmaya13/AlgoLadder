from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Custom_User


class SignUpForm(UserCreationForm):
    fullname = forms.CharField(max_length=200,help_text= 'Required.', label='Full Name')
    email = forms.EmailField(max_length=254, help_text='Required.',label='Email Address')
    #university = forms.CharField(max_length=30, help_text='Required.')
    phone = forms.CharField(max_length=30, help_text='Required.',label='Mobile Number')
    


class Meta:
        model = User
        fields = ('fullname','username', 'email', 'phone', 'password1')


class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class phoneUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = Custom_User
        fields = ['phone']



class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Custom_User
        fields = ['image']