from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name=forms.CharField(required=True,label="First Name",widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name=forms.CharField(required=False,label="Last Name",widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    
    class Meta:
        model=User
        fields=("first_name","last_name","email","username","password1","password2")

        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Username'}),
            'password1':forms.TextInput(attrs={'placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password'})
        }

    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username=forms.CharField(required=True,label='Username',widget=forms.TextInput(attrs={'placeholder':"Username"}))
    password=forms.CharField(required=True,label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    
    

