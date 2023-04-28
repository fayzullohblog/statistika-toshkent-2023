from ..models import Account
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import login,authenticate


class AccountForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    username = forms.CharField(max_length=50, widget=forms.TextInput)


    def clean_username(self):
        username = self.cleaned_data['username']
        r = Account.objects.filter(username=username)
        print('username', username)
        if r.count():
            raise ValidationError('Username Already exist')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        r = Account.objects.filter(email=email)
        print('email', email)
        if r.count():
            raise ValidationError('Email Already exist')
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
       
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = Account.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'], )
        print('useer', user)
        return user
    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'id':'username','name':'username'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'id':'password','name':'password'}))

    # def clean_password(self):
    #     username=self.cleaned_data['username']
    #     password=self.cleaned_data['password']
    #     print('---form',username,password)


    


   



