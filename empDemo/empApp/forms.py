from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField(required=False,validators=
    [validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastName = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password= forms.CharField(widget=forms.PasswordInput)
    salary = forms.CharField()
    ssn=forms.IntegerField