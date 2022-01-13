from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class AddRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['cat'].empty_label = 'empty'
        # self.fields['cat'].blank = True

    class Meta:
        model = Recipe
        # fields = ['name', 'photo', 'content', 'cat', 'ingr']
        fields = ['name', 'photo', 'content', 'cat', 'ingr']
        widgets = {
            'name': forms.TextInput(attrs={
             'class': "form-control", 'id': "exampleInputEmail1",
             'aria-describedby': "emailHelp", 'placeholder': 'Title', 'style': 'width: 30%'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'cat': forms.CheckboxSelectMultiple,
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('Name is too long: must be less than 50 characters')
        return name


class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'photo', 'content', 'cat', 'ingr']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': "form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': 'username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': "form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': '@ email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': 'password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': 'password confirmation'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':"form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': 'username'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'id': "exampleInputEmail1",
        'aria-describedby': "emailHelp", 'placeholder': 'password'}))
