from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordResetForm
from .models import Users



class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your confirm password'}))
    class Meta:
        model = Users
        fields = (
            'username',
            'email',
            'password',
        )
        
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your password'}),
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your email address'}),
            'username': forms.TextInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your username'}),
        }
        
        error_messages = {
            'username': {
                'unique': 'A user with that username already exists',
                'required': 'you must provide a username',
            },
            'email': {
                'unique': 'A user with that email already exists',
                'required': 'you must provide an email',
            },
            
        }
        
        def clean_password(self):
            password1 = self.cleaned_data.get("password")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")    
            return password2


class AcceptCodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'Enter your code'}),
        label=_('code'),
        error_messages={
            'required': _('this field is required'),
            'invalid': _('this field is invalid'),
        },
    )
    
    
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100,
                            error_messages={'required': _('Please enter email address')},
                            widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your email address'}))
    password = forms.CharField(min_length=8,
                               error_messages={'required': _('Please enter Your password')},
                            widget=forms.PasswordInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your password'}))
    
    
class PasswordResetForms(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'input input-bordered w-full my-2',"autocomplete": "email", 'placeholder': 'Enter your email'}),
    )


class EditProfile(forms.ModelForm):
    class Meta:
        model = Users
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'about_us',
            'image',
        )
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your email address'}),
            'username': forms.TextInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your username'}),
            'first_name': forms.TextInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your last name'}),
            'about_us': forms.Textarea(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your about us'}),
            'image': forms.FileInput(attrs={'class': 'input input-bordered w-full my-2', 'placeholder': 'enter your image'}),
        }
        
        error_messages = {
            'username': {
                'unique': 'A user with that username already exists',
                'required': 'you must provide a username',
            },
            'email': {
                'unique': 'A user with that email already exists',
                'required': 'you must provide an email',
            },
            'first_name': {
                'required': 'you must provide an first name',
            },
            'last_name': {
                'required': 'you must provide an last_name',
            },
            'about_us': {
                'required': 'you must provide an bio',
            },
            'image': {
                'required': 'you must provide an image'
            },
            }